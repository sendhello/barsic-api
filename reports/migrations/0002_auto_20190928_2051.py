# Generated by Django 2.1.12 on 2019-09-28 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarequest',
            name='request_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 28, 17, 51, 4, 353194), verbose_name='Дата создания'),
        ),
    ]