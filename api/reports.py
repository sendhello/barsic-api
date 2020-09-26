import logging
from decimal import Decimal

from .base_classes import BaseReport
from .helper import check_date_params, check_bool_params, get_company, convert_total_reports_to_product_dict
from settings.models import Tariff

logger = logging.getLogger(__name__)


class PeopleInZone(BaseReport):
    def __init__(self, *args, **kwargs):
        super(PeopleInZone, self).__init__(*args, **kwargs)
        self.report_type = 'people_in_zone'

    def query(self):
        rows = self._query(
            request=f"""
                {''}SELECT
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
                """
        )
        self.data.report = {row[2]: row[1] for row in rows} or {'Все зоны': 0}
        self.status = 'ok' if not self.status else self.status
        return self


class Companies(BaseReport):
    def __init__(self, *args, **kwargs):
        super(Companies, self).__init__(*args, **kwargs)
        self.report_type = 'companies'

    def query(self):
        super_account_type = 1
        rows = self._query(
            request=f"""{''}
                SELECT
                    SuperAccountId, Descr, Address, Inn, Email, Phone, WebSite
                FROM
                    SuperAccount
                WHERE
                    Type={super_account_type}
                """
        )
        if not rows:
            self.status = 'error'
            self.errors.append(f'Не найдено ни одной организации в БД "{self.data.db_name}"')
            return self

        self.data.report = {
            row[0]: {
                'name': row[1],
                'address': row[2],
                'inn': row[3],
                'email': row[4],
                'tel': row[5],
                'site': row[6]
            } for row in rows
        }
        self.status = 'ok'
        return self


class TotalReport(BaseReport):
    def __init__(self, company_id, date_from=None, date_to=None, hide_zero=None, hide_internal=None, *args, **kwargs):
        super(TotalReport, self).__init__(*args, **kwargs)
        self.report_type = 'total_report'
        self.company_id = company_id
        self.data.date_from, self.data.date_to, errors = check_date_params(date_from, date_to)
        self.errors += errors
        self.data.hide_zero, errors = check_bool_params(hide_zero)
        self.errors += errors
        self.data.hide_internal, errors = check_bool_params(hide_internal, default='1')
        self.errors += errors

    def query(self):
        if self.errors:
            self.status = 'error'
            return self

        companies = Companies(self.db_type).query().data.report
        self.data.company_name, errors = get_company(self.company_id, companies)
        self.errors += errors
        if self.errors:
            self.status = 'error'
            return self

        rows = self._query(
            request=f"exec sp_reportOrganizationTotals_v2 @sa={self.company_id},"
                    f"@from='{self.data.date_from.strftime('%Y%m%d 00:00:00')}',"
                    f"@to='{self.data.date_to.strftime('%Y%m%d 00:00:00')}',@hideZeroes={self.data.hide_zero},"
                    f"@hideInternal={self.data.hide_internal}"
        )
        if not rows:
            self.status = 'empty'
            self.data.report['Итого'] = Decimal('0.00')
            return self

        for row in rows:
            service_type = row[7] if row[7] else 'Прочее'
            service_group = row[6] if row[6] else 'Без группы'
            service_name = row[4]
            count = int(row[1]) if row[1] else 0
            summ = row[0] if row[0] else Decimal('0.00')
            if not self.data.report.get(service_type):
                self.data.report[service_type] = {}
            if not self.data.report[service_type].get(service_group):
                self.data.report[service_type][service_group] = {}
            self.data.report[service_type][service_group][service_name] = {
                'count': count,
                'sum': summ
            }

        self.status = 'ok'
        return self


class ClientCountReport(BaseReport):
    def __init__(self, company_id, date_from=None, date_to=None, *args, **kwargs):
        super(ClientCountReport, self).__init__(*args, **kwargs)
        self.report_type = 'client_count_report'
        self.company_id = company_id
        self.data.date_from, self.data.date_to, errors = check_date_params(date_from, date_to)
        self.errors += errors

    def query(self):
        if self.errors:
            self.status = 'error'
            return self

        companies = Companies(self.db_type).query().data.report
        self.data.company_name, errors = get_company(self.company_id, companies)
        self.errors += errors
        if self.errors:
            self.status = 'error'
            return self

        rows = self._query(
            request=f"exec sp_reportClientCountTotals @sa={self.company_id},"
                    f"@from='{self.data.date_from.strftime('%Y%m%d 00:00:00')}',"
                    f"@to='{self.data.date_to.strftime('%Y%m%d 00:00:00')}',@categoryId=0"
        )
        if not rows:
            self.status = 'empty'
            return self

        self.status = 'ok'
        self.data.report = {row[0].strftime('%Y-%m-%d'): row[1] for row in rows}
        return self


class ServicePointsReport(BaseReport):
    def __init__(self, *args, **kwargs):
        super(ServicePointsReport, self).__init__(*args, **kwargs)
        self.report_type = 'service_points_report'

    def query(self):
        rows = self._query(
            request=f"{''}SELECT ServicePointId, Name, SuperAccountId, Type, Code, IsInternal "
                    f"FROM ServicePoint"
        )
        if not rows:
            self.status = 'empty'
            return self

        report = {}
        for row in rows:
            report[row[0]] = {
                'name': row[1],
                'company_id': row[2],
                'type': row[3],
                'is_local': row[5]
            }

        self.status = 'ok'
        self.data.report = report
        return self


class CashReport(BaseReport):
    def __init__(self, date_from=None, date_to=None, *args, **kwargs):
        super(CashReport, self).__init__(*args, **kwargs)
        self.report_type = 'cash_report'
        self.data.date_from, self.data.date_to, errors = check_date_params(date_from, date_to)
        self.errors += errors

    def query(self):
        if self.errors:
            self.status = 'error'
            return self

        rows = self._query(
            request=f"exec sp_reportCashDeskMoney "
                    f"@from='{self.data.date_from.strftime('%Y%m%d 00:00:00')}', "
                    f"@to='{self.data.date_to.strftime('%Y%m%d 00:00:00')}'"
        )
        if not rows:
            self.status = 'empty'
            return self

        report = {}
        colums = ['service_point', 'sum', 'cash', 'bank', 'inside', 'bonus', 'lsi']
        generator = {colum: Decimal(0.0) for colum in colums[1:]}
        service_points = ServicePointsReport(db_type=self.db_type).query().data.report
        for row in rows:
            report.setdefault(row[-1], [])
            report.setdefault('total_sum', {'service_point': 'Итого по отчету', **generator})
            section_sum = report[row[-1]].pop() if report[row[-1]] else {'service_point': 'Итого', **generator}
            report[row[-1]].append({
                'service_point': service_points[row[0]]['name'],
                **{colums[i]: row[i] for i in range(1, len(colums))}
            })
            section_sum = {
                colums[i]: section_sum[colums[i]] + row[i]
                if isinstance(section_sum[colums[i]], Decimal)
                else section_sum[colums[i]]
                for i in range(len(colums))
            }
            report[row[-1]].append(section_sum)
            total_sum = report['total_sum']
            report['total_sum'] = {
                colums[i]: total_sum[colums[i]] + row[i]
                if isinstance(total_sum[colums[i]], Decimal)
                else total_sum[colums[i]]
                for i in range(len(colums))
            }

        self.status = 'ok'
        self.data.report = report
        return self


class BitrixReport(BaseReport):
    def __init__(self, date_from=None, date_to=None, *args, **kwargs):
        super(BitrixReport, self).__init__(*args, **kwargs)
        self.report_type = 'bitrix_report'
        self.data.date_from, self.data.date_to, errors = check_date_params(date_from, date_to)
        self.errors += errors

    def query(self):
        if self.errors:
            self.status = 'error'
            return self

        rows = self._query(
            request=f"""{''}
                SELECT Id, OrderNumber, ProductId, ProductName, OrderDate, PayDate, Sum, Pay, Status, Client
                FROM Transactions
                WHERE (PayDate >= '{self.data.date_from.strftime('%Y%m%d 00:00:00')}')
                    and(PayDate < '{self.data.date_to.strftime('%Y%m%d 00:00:00')}')
            """
        )

        if not rows:
            self.status = 'empty'
            return self

        self.status = 'ok'
        self.data.report = {
            'count': len(rows),
            'sum': sum(float(row[6]) for row in rows)
        }
        return self


class FinanceReport(BaseReport):
    def __init__(self, date_from=None, date_to=None, *args, **kwargs):
        super(FinanceReport, self).__init__(db_type='', *args, **kwargs)
        self.report_type = 'finance_report'
        self.data.date_from, self.data.date_to, errors = check_date_params(date_from, date_to)
        self.errors += errors

    def query(self):
        if self.errors:
            self.status = 'error'
            return self

        companies = Companies('aqua').query()

        total_reports = []
        for company_id in companies.data.report:
            report = TotalReport(
                db_type='aqua',
                company_id=company_id,
                date_from=self.data.date_from.strftime('%Y-%m-%d'),
                date_to=self.data.date_to.strftime('%Y-%m-%d'),
                hide_zero=self.data.hide_zero,
                hide_internal=self.data.hide_internal
            ).query()
            total_reports.append(report)

        report_bitrix = BitrixReport(
            db_type='bitrix',
            date_from=self.data.date_from.strftime('%Y-%m-%d'),
            date_to=self.data.date_to.strftime('%Y-%m-%d')
        ).query()

        products = convert_total_reports_to_product_dict(total_reports)

        report = {}
        for tariff in Tariff.objects.all():
            category = tariff.finance_report_category.title
            elem = report.setdefault(category, {'count': 0, 'sum': 0})

            if tariff.title in products:
                elem['count'] += 0 if tariff.title == 'Депозит' \
                    else products[tariff.title]['count']
                elem['sum'] += products[tariff.title]['sum']

            if tariff.title == 'Битрикс':
                elem['count'] += report_bitrix.data.report['count']
                elem['sum'] += report_bitrix.data.report['sum']

        self.status = 'ok'
        self.data.report = report
        return self
