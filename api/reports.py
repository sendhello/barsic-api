import logging
from datetime import datetime, timedelta
from decimal import Decimal

from settings.models import DataBase
from .base_classes import BaseReport, CompaniesData
from .helper import check_date_params, check_bool_params, get_company

logger = logging.getLogger(__name__)


class PeopleInZone(BaseReport):
    def __init__(self):
        super(PeopleInZone, self).__init__()
        self.report_type = 'people_in_zone'

    def query(self):
        db_type = 'aqua'
        db = DataBase.objects.filter(type=db_type).first()
        cursor, errors = self.get_cursor(db, db_type=db_type)
        if errors:
            self.status = 'error'
            self.errors += errors
            return self

        cursor.execute(
            f"""{''}
                SELECT
                    [gr].[c1] as [c11],
                    [gr].[StockCategory_Id] as [StockCategory_Id1],
                    [c].[Name],
                    [c].[NN]
                FROM
                    (
                        SELECT
                            [_].[CategoryId] as [StockCategory_Id],
                            Count(*) as [c1]
                        FROM
                            [AccountStock] [_]
                                INNER JOIN [SuperAccount] [t1] ON [_].[SuperAccountId] = [t1].[SuperAccountId]
                        WHERE
                            [_].[StockType] = 41 AND
                            [t1].[Type] = 0 AND
                            [_].[Amount] > 0 AND
                            NOT ([t1].[IsStuff] = 1)
                        GROUP BY
                            [_].[CategoryId]
                    ) [gr]
                        INNER JOIN [Category] [c] ON [gr].[StockCategory_Id] = [c].[CategoryId]
            """)
        rows = cursor.fetchall()

        if rows:
            self.data.report = {row[2]: row[1] for row in rows}
        else:
            self.data.report = {'Все зоны': 0}
        self.status = 'ok'
        return self


class Companies(BaseReport):
    def __init__(self):
        super(Companies, self).__init__()
        self.report_type = 'companies'

    def query(self, db_type):
        super_account_type = 1
        db = DataBase.objects.filter(type=db_type).first()
        cursor, errors = self.get_cursor(db, db_type=db_type)
        if errors:
            self.status = 'error'
            self.errors += errors
            return self

        self.data.db_name = db.title
        cursor.execute(
            f"""{''}
            SELECT
                SuperAccountId, Descr, Address, Inn, Email, Phone, WebSite
            FROM
                SuperAccount
            WHERE
                Type={super_account_type}
            """)
        rows = cursor.fetchall()
        if not rows:
            self.status = 'error'
            self.errors.append(f'Не найдено ни одной организации в БД "{db.title}"')
            return self

        self.data.report = {row[0]: CompaniesData(
            name=row[1],
            address=row[2],
            inn=row[3],
            email=row[4],
            tel=row[5],
            site=row[6]
        ) for row in rows}
        self.status = 'ok'
        return self


class TotalReport(BaseReport):
    def __init__(self):
        super(TotalReport, self).__init__()
        self.report_type = 'total_report'

    def query(self, db_type, company_id, date_from=None, date_to=None, hide_zero=None, hide_internal=None):
        db = DataBase.objects.filter(type=db_type).first()
        cursor, errors = self.get_cursor(db, db_type=db_type)
        self.errors += errors
        self.data.db_name = db.title
        self.data.date_from, self.data.date_to, errors = check_date_params(date_from, date_to)
        self.errors += errors
        self.data.hide_zero, errors = check_bool_params(hide_zero)
        self.errors += errors
        self.data.hide_internal, errors = check_bool_params(hide_internal, default='1')
        self.errors += errors
        if self.errors:
            self.status = 'error'
            return self

        companies = Companies().query(db_type=db_type).data.report
        self.data.company_name, errors = get_company(company_id, companies)
        self.errors += errors
        if self.errors:
            self.status = 'error'
            return self

        cursor.execute(f"exec sp_reportOrganizationTotals_v2 @sa={company_id},"
                       f"@from='{self.data.date_from.strftime('%Y%m%d 00:00:00')}',"
                       f"@to='{self.data.date_to.strftime('%Y%m%d 00:00:00')}',@hideZeroes={self.data.hide_zero},"
                       f"@hideInternal={self.data.hide_internal}")
        rows = cursor.fetchall()
        if not rows:
            self.status = 'ok'
            self.data.report['Итого'] = Decimal('0.00')
            return self

        for row in rows:
            service_type = row[7] if row[7] else 'Прочее'
            service_group = row[6] if row[6] else 'Без группы'
            service_name = row[4]
            count = int(row[1]) if row[1] else 0
            summ = row[0] if row[0] else Decimal('0.00')
            if not self.data.report.get(service_type):
                self.data.report[service_type] = {}
            if not self.data.report[service_type].get(service_group):
                self.data.report[service_type][service_group] = {}
            self.data.report[service_type][service_group][service_name] = {
                'count': count,
                'sum': summ
            }

        self.status = 'ok'
        return self


class ClientCount(BaseReport):
    def __init__(self, db, date_from=None, date_to=None):
        super(ClientCount, self).__init__(db)
        if date_from is None:
            date_from = datetime.now().strftime('%Y%m%d 00:00:00')
        self.date_from = date_from
        if date_to is None:
            date_to = (datetime.now() + timedelta(1)).strftime('%Y%m%d 00:00:00')
        self.date_to = date_to

    def query(self, db_type:str):
        db = DataBase.objects.filter(type=db_type).first()
        cursor, errors = self.get_cursor(db, db_type=db_type)
        if errors:
            self.status = 'error'
            self.errors += errors
            return None
        company = Companies().get_first_company()
        cursor.execute(
            f"exec sp_reportClientCountTotals @sa={company.company_id},"
            f"@from='{self.date_from}',@to='{self.date_to}',@categoryId=0"
        )
        rows = cursor.fetchall()
        if not rows:
            return {}
        return self.to_json(rows)

    def to_json(self, rows):
        report = {}
        for row in rows:
            date = row[0].strftime('%Y%m%d')
            report[date] = row[1]
        return report

