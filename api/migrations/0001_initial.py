# Generated by Django 3.1.5 on 2021-01-16 14:24

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=128, unique=True, verbose_name='Дата')),
                ('weekday', models.CharField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], max_length=1, verbose_name='День недели')),
                ('clients_count', models.PositiveIntegerField(default=0, verbose_name='Количество проходов')),
                ('total_sum', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=11, verbose_name='Общая сумма')),
                ('deposit_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Депозит')),
                ('ticket_count', models.PositiveIntegerField(default=0, verbose_name='Билеты | Количество')),
                ('ticket_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Билеты | Сумма')),
                ('terms_count', models.PositiveIntegerField(default=0, verbose_name='Термозона | Количество')),
                ('terms_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Термозона | Сумма')),
                ('catering_count', models.PositiveIntegerField(default=0, verbose_name='Общепит | Количество')),
                ('catering_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Общепит | Сумма')),
                ('corp_ticket_count', models.PositiveIntegerField(default=0, verbose_name='Билеты КОРП | Количество')),
                ('corp_ticket_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Билеты КОРП | Сумма')),
                ('corp_terms_count', models.PositiveIntegerField(default=0, verbose_name='Термозона КОРП | Количество')),
                ('corp_terms_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Термозона КОРП | Сумма')),
                ('reg_ticket_count', models.PositiveIntegerField(default=0, verbose_name='Билеты РЕГ | Количество')),
                ('reg_ticket_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Билеты РЕГ | Сумма')),
                ('reg_terms_count', models.PositiveIntegerField(default=0, verbose_name='Термозона РЕГ | Количество')),
                ('reg_terms_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Термозона РЕГ | Сумма')),
                ('others_count', models.PositiveIntegerField(default=0, verbose_name='Прочее | Количество')),
                ('others_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Прочее | Сумма')),
                ('online_count', models.PositiveIntegerField(default=0, verbose_name='Online продажи | Количество')),
                ('online_sum', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='Online продажи | Сумма')),
            ],
            options={
                'verbose_name': 'финансовый отчеты',
                'verbose_name_plural': 'финансовые отчеты',
            },
        ),
    ]