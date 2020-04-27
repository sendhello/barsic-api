import logging
from typing import Optional, Tuple, List, Any
from datetime import datetime

import pyodbc

from settings.models import DataBase
from typing import Dict, List

logger = logging.getLogger(__name__)


class BaseData(object):
    def __init__(self):
        pass


class Data(BaseData):
    def __init__(self, zones=None, companies=None, db_name=None, total_report=None, company_name=None, date_from=None,
                 date_to=None, hide_zero=None, hide_internal=None):
        super(Data, self).__init__()
        self.zones: List = zones
        self.companies: List = companies
        self.db_name: str = db_name
        self.company_name: str = company_name
        self.date_from: datetime = date_from
        self.date_to: datetime = date_to
        self.hide_zero: bool = hide_zero
        self.hide_internal: bool = hide_internal
        self.total_report: List = total_report


class PeoplesInZoneData(BaseData):
    def __init__(self, zone, people_count):
        super(PeoplesInZoneData, self).__init__()
        self.zone: str = zone
        self.people_count: int = people_count


class CompaniesData(BaseData):
    def __init__(self, company_id, name, address, inn, email, tel, site):
        super(CompaniesData, self).__init__()
        self.id: int = company_id
        self.name: str = name
        self.address: str = address
        self.inn: str = inn
        self.email: str = email
        self.tel: str = tel
        self.site: str = site


class BaseReport(object):
    def __init__(self):
        self.status = 'undefined'
        self.errors = []
        self.data = Data()

    @staticmethod
    def get_cursor(db: DataBase) -> Tuple[Optional[Any], List]:
        errors = []
        if not db:
            errors.append(f'База данных не определена')
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