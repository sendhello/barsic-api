import logging
from datetime import datetime, timedelta
from .base_classes import BaseRequest, Data, PeoplesInZoneData, CompaniesData

logger = logging.getLogger(__name__)


class PeoplesInZoneReport(BaseRequest):
    def __init__(self):
        super(PeoplesInZoneReport, self).__init__()
        self.data.zones = []

    def query(self):
        database_type = 'aqua'
        cursor, errors = self.get_cursor(database_type)
        if errors:
            self.status = 'error'
            self.errors += errors
            return None

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


class CompaniesReport(BaseRequest):
    def __init__(self):
        super(CompaniesReport, self).__init__()
        self.data.companies = []

    def query(self, database_type: str):
        super_account_type = 1
        cursor, errors = self.get_cursor(database_type)
        if errors:
            self.status = 'error'
            self.errors += errors
            return None

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
            self.errors.append(f'Не найдено ни одной организации в БД типа "{database_type}"')
        else:
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

    def get_first_company(self):
        return self.data.companies[0]


class TotalReport(BaseRequest):
    def __init__(self, db, date_from=None, date_to=None, hide_zero=None, hide_internal=None):
        super(TotalReport, self).__init__(db)
        if date_from is None:
            date_from = datetime.now().strftime('%Y%m%d 00:00:00')
        self.date_from = date_from
        if date_to is None:
            date_to = (datetime.now() + timedelta(1)).strftime('%Y%m%d 00:00:00')
        self.date_to = date_to
        if hide_zero is None:
            hide_zero = 0
        self.hide_zero = hide_zero
        if hide_internal is None:
            hide_internal = 1
        self.hide_internal = hide_internal

    def query(self, database_type: str):
        cursor, errors = self.get_cursor(database_type)
        if errors:
            self.status = 'error'
            self.errors += errors
            return None
        company = CompaniesReport().get_first_company()
        cursor.execute(
            f"exec sp_reportOrganizationTotals_v2 @sa={company.company_id},@from='{self.date_from}',"
            f"@to='{self.date_to}',@hideZeroes={self.hide_zero},@hideInternal={self.hide_internal}"
            )
        rows = cursor.fetchall()
        if not rows:
            return {}
        return self.to_json(rows)

    def to_json(self, rows):
        total_report = {}
        for row in rows:
            try:
                total_report[row[7]]
            except KeyError:
                total_report[row[7]] = {}
            try:
                total_report[row[7]][row[6]]
            except KeyError:
                total_report[row[7]][row[6]] = {}
            total_report[row[7]][row[6]][row[4]] = {
                'count': row[1],
                'sum': row[0]
            }
        return total_report


class ClientCountReport(BaseRequest):
    def __init__(self, db, date_from=None, date_to=None):
        super(ClientCountReport, self).__init__(db)
        if date_from is None:
            date_from = datetime.now().strftime('%Y%m%d 00:00:00')
        self.date_from = date_from
        if date_to is None:
            date_to = (datetime.now() + timedelta(1)).strftime('%Y%m%d 00:00:00')
        self.date_to = date_to

    def query(self):
        cursor, errors = self.get_cursor(database_type)
        if errors:
            self.status = 'error'
            self.errors += errors
            return None
        company = CompaniesReport().get_first_company()
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

