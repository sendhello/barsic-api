import logging
import pyodbc
from datetime import datetime
from threading import Thread, Event
from settings.models import DataBases, SettingBase
import json


def log_info(message):
    return logging.info(f'{__name__}: {str(datetime.now())[:-7]}:    {message}')


def log_error(message):
    return logging.error(f'{__name__}: {str(datetime.now())[:-7]}:    Ошибка {message}')


def get_connect_string(db_id):
    db = DataBases.objects.get(id=db_id)
    connect_string = f'DRIVER={db.driver};SERVER={db.server};DATABASE={db.database};UID={db.user};PWD={db.pwd}'
    return connect_string


def convert_to_dict(zones_list):
    zones = {'zones': []}
    for zone in zones_list:
        zones['zones'].append({
            'zone': zone[2],
            'peoples': zone[0]
        })
    return zones


def db_connect(connect_string):
    try:
        log_info('Попытка соединения')
        connect = pyodbc.connect(connect_string)
    except pyodbc.OperationalError as e:
        log_error(repr(e))
        return None
    except pyodbc.ProgrammingError as e:
        log_error(repr(e))
        return None
    return connect


def sql_query():
    db_id = 1
    connect_string = get_connect_string(db_id)
    connect = db_connect(connect_string)
    if not connect:
        return convert_to_dict([('--', 488, 'Error', ''), ])
    cursor = connect.cursor()
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
        return convert_to_dict([('0', 488, 'Все зоны', '0003'), ])
    return convert_to_dict(rows)


class ClientCountNow(object):
    """Количество посетителей в зоне сейчас"""
    def __init__(self, database):
        logging.info(f'{__name__}: {str(datetime.now())[:-7]}:    Создание объекта "ClientCountNow", база {database}')
        stop_event = Event()
        self.__Request = []
        def run_sql_query():
            self.__Request = sql_query(database)
        action_thread = Thread(target=run_sql_query)
        action_thread.start()
        action_thread.join(timeout=5)
        stop_event.set()
        if not self.__Request:
            self.__Request.append(('--', 488, 'Error', 'Ошибка соединения'))

    @property
    def count_clients_all_zones(self):
        """
        :return: Dict: Словарь зон с количеством людей
        """
        result = {}
        for element in self.__Request:
            result[element[2]] = element[0]
        return result

    @property
    def count_clients_first_zone(self):
        """:return: tuple: Пара <Первая зона в организации>, <Количество посетителей>"""
        return self.__Request[0][2], self.__Request[0][0]
