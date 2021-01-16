from django.db import models
from decimal import Decimal


class FinanceReport(models.Model):
    DAYS_OF_WEEK = (
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье')
    )

    date = models.DateField('Дата', max_length=128, unique=True)
    weekday = models.CharField('День недели', max_length=1, choices=DAYS_OF_WEEK)
    clients_count = models.PositiveIntegerField('Количество проходов', default=0)
    total_sum = models.DecimalField('Общая сумма', decimal_places=2, max_digits=11, default=Decimal(0))
    deposit_sum = models.DecimalField('Депозит', decimal_places=2, max_digits=11, default=0)
    ticket_count = models.PositiveIntegerField('Билеты | Количество', default=0)
    ticket_sum = models.DecimalField('Билеты | Сумма', decimal_places=2, max_digits=11, default=0)
    terms_count = models.PositiveIntegerField('Термозона | Количество', default=0)
    terms_sum = models.DecimalField('Термозона | Сумма', decimal_places=2, max_digits=11, default=0)
    catering_count = models.PositiveIntegerField('Общепит | Количество', default=0)
    catering_sum = models.DecimalField('Общепит | Сумма', decimal_places=2, max_digits=11, default=0)
    corp_ticket_count = models.PositiveIntegerField('Билеты КОРП | Количество', default=0)
    corp_ticket_sum = models.DecimalField('Билеты КОРП | Сумма', decimal_places=2, max_digits=11, default=0)
    corp_terms_count = models.PositiveIntegerField('Термозона КОРП | Количество', default=0)
    corp_terms_sum = models.DecimalField('Термозона КОРП | Сумма', decimal_places=2, max_digits=11, default=0)
    reg_ticket_count = models.PositiveIntegerField('Билеты РЕГ | Количество', default=0)
    reg_ticket_sum = models.DecimalField('Билеты РЕГ | Сумма', decimal_places=2, max_digits=11, default=0)
    reg_terms_count = models.PositiveIntegerField('Термозона РЕГ | Количество', default=0)
    reg_terms_sum = models.DecimalField('Термозона РЕГ | Сумма', decimal_places=2, max_digits=11, default=0)
    others_count = models.PositiveIntegerField('Прочее | Количество', default=0)
    others_sum = models.DecimalField('Прочее | Сумма', decimal_places=2, max_digits=11, default=0)
    online_count = models.PositiveIntegerField('Online продажи | Количество', default=0)
    online_sum = models.DecimalField('Online продажи | Сумма', decimal_places=2, max_digits=11, default=0)

    class Meta:
        verbose_name = 'финансовый отчеты'
        verbose_name_plural = 'финансовые отчеты'

    def __str__(self):
        return f"Финансовый отчеты за {self.date}"