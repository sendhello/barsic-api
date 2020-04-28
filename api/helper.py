from typing import Optional, Tuple, List
from datetime import datetime, timedelta


def check_date_params(date_from: Optional[str], date_to: Optional[str]) -> Tuple:
    errors = []
    if date_from is None:
        date_from = datetime.now()
    else:
        try:
            date_from = datetime.strptime(date_from, '%Y%m%d')
        except ValueError as e:
            errors.append(f'Неверный формат параметра date_from: {e}')

    if date_to is None:
        date_to = date_from + timedelta(1)
    else:
        try:
            date_to = datetime.strptime(date_to, '%Y%m%d')
        except ValueError as e:
            errors.append(f'Неверный формат параметра date_to: {e}')

    return date_from, date_to, errors


def check_bool_params(param: str, default: str='0'):
    errors = []
    alternative = '1' if default == '0' else '0'
    if param is None or param.isdigit() and param == default:
        param = default
    elif param.isdigit() and param == alternative:
        param = alternative
    else:
        errors.append(f'Параметр {param.__name__} должен быть равен 0 или 1')
    return param, errors


def get_company(company_id: str, companies: List):
    for company in companies:
        if str(company.id) == company_id:
            return company.name, []
    return None, [f'Не существует организации с id {company_id}']
