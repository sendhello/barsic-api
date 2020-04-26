import logging
from typing import Optional, Tuple, List, Any

import pyodbc

from settings.models import DataBase

logger = logging.getLogger(__name__)


class Data(object):
    def __init__(self):
        pass


class PeoplesInZoneData(Data):
    def __init__(self, zone, people_count):
        super(PeoplesInZoneData, self).__init__()
        self.zone: str = zone
        self.people_count: int = people_count


class CompaniesData(Data):
    def __init__(self, company_id, name, address, inn, email, tel, site):
        super(CompaniesData, self).__init__()
        self.id = company_id,
        self.name = name,
        self.address = address,
        self.inn = inn,
        self.email = email,
        self.tel = tel,
        self.site = site,


class BaseRequest(object):
    def __init__(self):
        self.status = 'undefined'
        self.errors = []
        self.data = Data()

    @staticmethod
    def get_cursor(db_type: str) -> Tuple[Optional[Any], List]:
        errors = []
        db = DataBase.objects.filter(type=db_type).first()
        if not db:
            errors.append(f'База данных с типом "{db_type}" не определена')
            return None, errors
        connect_string = f'DRIVER={db.driver};SERVER={db.server};DATABASE={db.database};UID={db.user};PWD={db.pwd}'
        try:
            logger.info(f'Попытка соединения c БД {db.title}')
            conn = pyodbc.connect(connect_string)
        except (pyodbc.OperationalError, pyodbc.ProgrammingError) as e:
            logger.error(repr(e))
            errors.append(repr(e))
            return None, errors

        return conn.cursor(), []
