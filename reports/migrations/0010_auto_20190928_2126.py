# Generated by Django 2.1.12 on 2019-09-28 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_auto_20190928_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 28, 18, 26, 29, 5513), verbose_name='Дата создания'),
        ),
    ]