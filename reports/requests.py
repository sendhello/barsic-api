import logging
from datetime import datetime, timedelta

import pyodbc


def log_info(message):
    return logging.info(f'{__name__}: {str(datetime.now())[:-7]}:    {message}')


def log_error(message):
    return logging.error(f'{__name__}: {str(datetime.now())[:-7]}:    Ошибка {message}')


class ConnectToDatabase(object):
    def __init__(self, database):
        self.db = database

    @property
    def connect_string(self):
        db = self.db
        connect_s = f'DRIVER={db.driver};SERVER={db.server};DATABASE={db.database};UID={db.user};PWD={db.pwd}'
        return connect_s

    def connect(self):
        try:
            log_info('Попытка соединения')
            conn = pyodbc.connect(self.connect_string)
        except pyodbc.OperationalError as e:
            log_error(repr(e))
            return None
        except pyodbc.ProgrammingError as e:
            log_error(repr(e))
            return None
        return conn

    def get_cursor(self):
        connect = self.connect()
        if not connect:
            return None
        return connect.cursor()

    def to_json(self, obj):
        return {}

    def query(self):
        return {}


class PeoplesInZoneReport(ConnectToDatabase):
    def query(self):
        cursor = self.get_cursor()
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
        if not rows:
            return self.to_json([('0', 488, 'Все зоны', '0003'), ])
        return self.to_json(rows)

    def to_json(self, rows):
        zones = {'zones': []}
        for row in rows:
            zones['zones'].append({
                'zone': row[2],
                'peoples': row[0]
            })
        return zones


class AllCompanyReport(ConnectToDatabase):
    def query(self):
        cursor = self.get_cursor()
        super_account_type = 1
        cursor.execute(
            f"""{''}
            SELECT
                SuperAccountId, Type, Descr, CanRegister, CanPass, IsStuff, IsBlocked, BlockReason, DenyReturn, 
                ClientCategoryId, DiscountCard, PersonalInfoId, Address, Inn, ExternalId, RegisterTime,
                LastTransactionTime, LegalEntityRelationTypeId, SellServicePointId, DepositServicePointId, 
                AllowIgnoreStoredPledge, Email, Latitude, Longitude, Phone, WebSite, TNG_ProfileId
            FROM
                SuperAccount
            WHERE
                Type={super_account_type}
            """)
        rows = cursor.fetchall()
        if not rows:
            return {}
        return self.to_json(rows)

    def to_json(self, rows):
        companies = {}
        for row in rows:
            companies[row[0]] = {
                'id': row[0],
                'name': row[2],
                'address': row[12],
                'inn': row[13],
                'email': row[21],
                'tel': row[24],
                'site': row[25],
            }
        return companies

    def get_first_company(self):
        for company in self.query():
            return company


class TotalReport(ConnectToDatabase):
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

    def query(self):
        cursor = self.get_cursor()
        company = AllCompanyReport(self.db).get_first_company()
        cursor.execute(
            f"exec sp_reportOrganizationTotals_v2 @sa={company},@from='{self.date_from}',"
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


class ClientCountReport(ConnectToDatabase):
    def __init__(self, db, date_from=None, date_to=None):
        super(ClientCountReport, self).__init__(db)
        if date_from is None:
            date_from = datetime.now().strftime('%Y%m%d 00:00:00')
        self.date_from = date_from
        if date_to is None:
            date_to = (datetime.now() + timedelta(1)).strftime('%Y%m%d 00:00:00')
        self.date_to = date_to

    def query(self):
        cursor = self.get_cursor()
        company = AllCompanyReport(self.db).get_first_company()
        cursor.execute(
            f"exec sp_reportClientCountTotals @sa={company},"
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

