import logging
from datetime import datetime

import pyodbc


def log_info(message):
    return logging.info(f'{__name__}: {str(datetime.now())[:-7]}:    {message}')


def log_error(message):
    return logging.error(f'{__name__}: {str(datetime.now())[:-7]}:    Ошибка {message}')


class ReportFromBase(object):
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

    def to_json(self, obj):
        return {}

    def query(self):
        return {}


class ReportPeoplesInZone(ReportFromBase):
    def to_json(self, obj):
        zones = {'zones': []}
        for zone in obj:
            zones['zones'].append({
                'zone': zone[2],
                'peoples': zone[0]
            })
        return zones

    def query(self):
        conn = self.connect()
        if not conn:
            return self.to_json([('--', 488, 'Error', ''), ])
        cursor = conn.cursor()
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
