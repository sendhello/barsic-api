from typing import Optional, Tuple, Dict, Any, List
from datetime import datetime, timedelta


def reset_time(dt: datetime) -> datetime:
    return datetime(year=dt.year, month=dt.month, day=dt.day)


def check_date_params(date_from: Optional[str], date_to: Optional[str]) -> Tuple:
    if date_from is None:
        date_from = reset_time(datetime.now())
    else:
        try:
            date_from = reset_time(datetime.strptime(date_from, '%Y-%m-%d'))
        except ValueError as e:
            return None, None, [f'Неверный формат параметра date_from: {e}']

    if date_to is None:
        date_to = reset_time(date_from + timedelta(1))
    else:
        try:
            date_to = reset_time(datetime.strptime(date_to, '%Y-%m-%d'))
        except ValueError as e:
            return None, None, [f'Неверный формат параметра date_to: {e}']

    return date_from, date_to, []


def check_bool_params(param: str, default: str = '0'):
    errors = []
    alternative = '1' if default == '0' else '0'
    if param is None or param.isdigit() and param == default:
        param = default
    elif param.isdigit() and param == alternative:
        param = alternative
    else:
        errors.append(f'Параметр {param.__name__} должен быть равен 0 или 1')
    return param, errors


def get_company(company_id: str, companies: Dict):
    if int(company_id) in companies:
        return companies[int(company_id)]['name'], []
    return None, [f'Не существует организации с id {company_id}']


def convert_total_reports_to_product_dict(total_reports: List):
    products = {}
    for total_report in total_reports:
        for _, product_groups in total_report.data.report.items():
            for _, product_group in product_groups.items():
                for product_name, product in product_group.items():
                    products[product_name] = product

    return products
