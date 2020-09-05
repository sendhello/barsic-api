import logging
from datetime import datetime
from typing import Optional, Tuple, List, Any, Dict

import pyodbc
from django.core.exceptions import ObjectDoesNotExist

from settings.models import DataBase

logger = logging.getLogger(__name__)


class BaseData(object):
    def __init__(self):
        pass


class Data(BaseData):
    def __init__(self, report=None, db_name=None, company_name=None, date_from=None,
                 date_to=None, hide_zero=None, hide_internal=None):
        super(Data, self).__init__()
        self.report: Dict = report
        self.db_name: str = db_name
        self.company_name: str = company_name
        self.date_from: datetime = date_from
        self.date_to: datetime = date_to
        self.hide_zero: bool = hide_zero
        self.hide_internal: bool = hide_internal


class PeoplesInZoneData(BaseData):
    def __init__(self, zone, people_count):
        super(PeoplesInZoneData, self).__init__()
        self.zone: str = zone
        self.people_count: int = people_count


class CompaniesData(BaseData):
    def __init__(self, name, address, inn, email, tel, site):
        super(CompaniesData, self).__init__()
        self.name: str = name
        self.address: str = address
        self.inn: str = inn
        self.email: str = email
        self.tel: str = tel
        self.site: str = site


class BaseReport(object):
    def __init__(self, db_type: str):
        self.db_type = db_type
        self.status = 'undefined'
        self.errors = []
        self.report_type = None
        self.data = Data()
        self.data.report = {}

    @staticmethod
    def get_cursor(db: DataBase) -> Tuple[Optional[Any], List]:
        connect_string = f'DRIVER={db.driver};SERVER={db.server},{db.port};DATABASE={db.database};UID={db.user};PWD={db.pwd}'
        conn = pyodbc.connect(connect_string)
        return conn.cursor()

    def _query(self, request: str) -> List[Any]:
        try:
            db = DataBase.objects.get(type=self.db_type)
        except ObjectDoesNotExist:
            self.errors.append(f'Не найдена база данных с алиасом {self.db_type}')
            self.status = 'error'
            return []

        try:
            cursor = self.get_cursor(db)
        except (pyodbc.OperationalError, pyodbc.ProgrammingError) as e:
            logger.error(repr(e))
            self.errors.append(repr(e))
            self.status = 'error'
            return []

        self.data.db_name = db.title
        cursor.execute(request)
        rows = cursor.fetchall()
        return rows

    def query(self):
        raise IndentationError
