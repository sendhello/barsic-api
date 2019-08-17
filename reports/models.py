from django.db import models
from datetime import datetime
from django.db import connections
import logging
import json


class DataRequest(models.Model):
    id = models.AutoField('Id', primary_key=True)
    request_date = models.DateTimeField('Дата создания', default=datetime.utcnow())
    time_type = models.CharField('Временной тип', max_length=254)
    date_from = models.DateTimeField('Начало периода')
    date_to = models.DateTimeField('Конец периода')
    data = models.TextField('Данные отчета в JSON')
    author = models.CharField('Инициатор запроса', max_length=100)

    class Meta:
        verbose_name = 'запись отчета'
        verbose_name_plural = 'Записи отчетов'

    def __str__(self):
        return 'ZZZZZZZ'

    def all_clients_in_zone(self):
        cursor = connections['aqua'].cursor
        with cursor() as cursor:
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
            response = cursor.fetchall()
        return response

    def request_base(self):
        cursor = connections['aqua'].cursor
        org = 36
        hide_zeroes = 0
        hide_internal = 1
        with cursor() as cursor:
            cursor.execute(
                f"""
                exec sp_reportOrganizationTotals_v2 @sa={org},@from='{self.date_from.strftime("%Y%m%d")}',
                @to='{self.date_to.strftime("%Y%m%d")}',@hideZeroes={hide_zeroes},@hideInternal={hide_internal}
                """)
            response = cursor.fetchall()
        response.append((0, 0, 0, 0, 'org_name', 0, 'Организация', 'Организация'))
        if len(response) > 1:
            print(
                f'{__name__}: {str(datetime.now())[:-7]}:    Итоговый отчет сформирован ID организации = {org}, '
                f'Период: {self.date_from}-{self.date_to}, Скрывать нули = {hide_zeroes}, .'
                f'Скрывать внутренние точки обслуживания: {hide_internal})')
        self.data = json.dumps(response)
        return 'Done!'

