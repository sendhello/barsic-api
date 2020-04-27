import logging
from datetime import datetime, timedelta
from .base_classes import BaseReport, BaseData, PeoplesInZoneData, CompaniesData
from settings.models import DataBase
from decimal import Decimal

logger = logging.getLogger(__name__)


class PeopleInZone(BaseReport):
    def __init__(self):
        super(PeopleInZone, self).__init__()
        self.data.zones = []

    def query(self):
        db_type = 'aqua'
        db = DataBase.objects.filter(type=db_type).first()
        cursor, errors = self.get_cursor(db)
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
            self.data.zones = [PeoplesInZoneData(zone=row[2], people_count=row[1]) for row in rows]
        else:
            self.data.zones.append(PeoplesInZoneData(zone='Все зоны', people_count=0))
        self.status = 'ok'
        return self


class Companies(BaseReport):
    def __init__(self):
        super(Companies, self).__init__()
        self.data.companies = []

    def query(self, db_type):
        super_account_type = 1
        db = DataBase.objects.filter(type=db_type).first()
        cursor, errors = self.get_cursor(db)
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

        self.data.companies = [
            CompaniesData(
                company_id=row[0],
                name=row[1],
                address=row[2],
                inn=row[3],
                email=row[4],
                tel=row[5],
                site=row[6]
            ) for row in rows
        ]
        self.status = 'ok'
        return self

    def get_first_company(self):
        return self.data.companies[0]


class TotalReport(BaseReport):
    def __init__(self):
        super(TotalReport, self).__init__()
        self.data.total_report = []

    def query(self, db_type, date_from=None, date_to=None, hide_zero=None, hide_internal=None):
        company = Companies().query(db_type=db_type).get_first_company()
        self.data.company_name = company.name
        db = DataBase.objects.filter(type=db_type).first()
        cursor, errors = self.get_cursor(db)
        if errors:
            self.status = 'error'
            self.errors += errors
            return self

        self.data.db_name = db.title
        if date_from is None:
            self.data.date_from = datetime.now()
        else:
            try:
                self.data.date_from = datetime.strptime(date_from, '%Y%m%d')
            except ValueError as e:
                self.status = 'error'
                self.errors.append(f'Неверный формат параметра date_from: {e}')
                return self
        if date_to is None:
            self.data.date_to = self.data.date_from + timedelta(1)
        else:
            try:
                self.data.date_to = datetime.strptime(date_to, '%Y%m%d')
            except ValueError as e:
                self.status = 'error'
                self.errors.append(f'Неверный формат параметра date_to: {e}')
                return self
        if hide_zero is None or hide_zero.isdigit() and hide_zero == '0':
            self.data.hide_zero = 0
        elif hide_zero.isdigit() and hide_zero == '1':
            self.data.hide_zero = 1
        else:
            self.status = 'error'
            self.errors.append('Параметр hide_zero должен быть равен 0 или 1')
            return self
        if hide_internal is None or hide_internal.isdigit() and hide_internal == '1':
            self.data.hide_internal = 1
        elif hide_internal.isdigit() and hide_internal == '0':
            self.data.hide_internal = 0
        else:
            self.status = 'error'
            self.errors.append('Параметр hide_internal должен быть равен 0 или 1')
            return self
        cursor.execute(f"exec sp_reportOrganizationTotals_v2 @sa={company.id},"
                       f"@from='{self.data.date_from.strftime('%Y%m%d 00:00:00')}',"
                       f"@to='{self.data.date_to.strftime('%Y%m%d 00:00:00')}',@hideZeroes={self.data.hide_zero},"
                       f"@hideInternal={self.data.hide_internal}")
        rows = cursor.fetchall()
        if not rows:
            self.status = 'ok'
            self.data.total_report['Итого'] = Decimal('0.00')
            return self

        for row in rows:
            self.data.total_report.append({
                'name': row[4],
                'count': row[1],
                'sum': row[0],
                'group': row[6],
                'type': row[7]
            })

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
        cursor, errors = self.get_cursor(db)
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

