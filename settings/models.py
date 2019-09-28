from django.db import models
from solo.models import SingletonModel


class SettingBase(SingletonModel):
    db_aqua = models.PositiveIntegerField(
        'ID БД Bars-Аквапарк',
        help_text='Числовой id из списка баз данных в разделе "Базы данных"',
        null=True,
        blank=True
    )
    db_beach = models.PositiveIntegerField(
        'ID БД Bars-Пляж',
        help_text='Числовой id из списка баз данных в разделе "Базы данных"',
        null=True,
        blank=True
    )
    db_bitrix = models.PositiveIntegerField(
        'ID БД заказов с сайта',
        help_text='Числовой id из списка баз данных в разделе "Базы данных"',
        null=True,
        blank=True
    )

    def __str__(self):
        return self._meta.verbose_name.title()

    class Meta:
        verbose_name = 'сопоставление баз данных'


class SettingBitrix(SingletonModel):
    url = models.SlugField(
        'Адрес сайта',
        help_text='Адрес сайта без "http://" и "/", например "exsample.com"',
        null=True
    )
    path = models.CharField(
        'Путь к обработчику 1С',
        max_length=255,
        help_text='Путь к обработчику 1С на сайте',
        default='/bitrix/admin/1c_exchange.php'
    )
    login = models.CharField(
        'Логин',
        max_length=255,
        help_text='Логин админки bitrix',
        null=True
    )
    password = models.CharField(
        'Пароль',
        max_length=255,
        help_text='Пароль админки bitrix',
        null=True
    )

    def __str__(self):
        return self._meta.verbose_name.title()

    class Meta:
        verbose_name = 'настройки Bitrix'


class SettingYandex(SingletonModel):
    token = models.CharField(
        'Yandex-токен',
        max_length=255,
        help_text='Yandex-токен',
        null=True,
    )
    path = models.CharField(
        'Путь к папке',
        max_length=255,
        help_text='Путь к папке в Yandex-Диске',
        default='/'
    )

    def __str__(self):
        return self._meta.verbose_name.title()

    class Meta:
        verbose_name = 'настройки Yandex.Disk'


class SettingGoogleSheets(SingletonModel):
    credentials_file = models.FileField(
        'JSON-token',
        upload_to='data/'
    )
    writers = models.TextField(
        'Список редакторов',
        help_text='Список email-адресов через запятую',
        null=True,
        blank=True
    )
    readers = models.TextField(
        'Список зрителей',
        help_text='Список email-адресов через запятую',
        null=True,
        blank=True
    )
    is_read_all = models.BooleanField(
        'Разрешить просмотр по ссылке для всех',
        default=False
    )

    def __str__(self):
        return self._meta.verbose_name.title()

    class Meta:
        verbose_name = 'настройки GoogleSheets'


class SettingTelegram(SingletonModel):
    token = models.CharField(
        'Telegram-токен',
        max_length=255,
        help_text='Telegram-токен',
        null=True,
    )
    chanel_id = models.IntegerField(
        'ID канала',
        help_text='ID пользователя или группы',
        null=True
    )
    is_proxy = models.BooleanField(
        'Использовать прокси',
        default=False
    )
    SOCKS4 = 'PROXY_TYPE_SOCKS4'
    SOCKS5 = 'PROXY_TYPE_SOCKS5'
    HTTP = 'PROXY_TYPE_HTTP'
    PROXY_TYPES = (
        (SOCKS5, 'SOCKS5'),
        (SOCKS4, 'SOCKS4'),
        (HTTP, 'HTTP'),
    )
    proxy_type = models.CharField(
        'Тип прокси',
        max_length=30,
        choices=PROXY_TYPES,
        default=SOCKS5
    )
    proxy_host = models.SlugField(
        'Адрес прокси-сервера',
        help_text='Адрес сервера без "http://" и "/"',
        null=True,
        blank=True
    )
    proxy_port = models.PositiveIntegerField(
        'Порт прокси сервера',
        help_text='ID пользователя или группы',
        null=True,
        blank=True,
        default=80
    )
    is_auth = models.BooleanField(
        'Нужна авторизация',
        default=False
    )
    username = models.CharField(
        'Логин прокси',
        max_length=255,
        help_text='Логин прокси сервера',
        null=True,
        blank=True
    )
    password = models.CharField(
        'Пароль прокси',
        max_length=255,
        help_text='Пароль прокси сервера',
        null=True,
        blank=True
    )

    def __str__(self):
        return self._meta.verbose_name.title()

    class Meta:
        verbose_name = 'настройки Telegram'


class DataBases(models.Model):
    """Класс настроек подключений к БД Барса и Битрикса"""
    class Meta:
        verbose_name = 'базу данных'
        verbose_name_plural = 'Базы данных'

    database = models.CharField('Имя базы данных', max_length=254)
    server = models.CharField('Сервер', max_length=254)
    user = models.CharField('Имя пользователя', max_length=254)
    pwd = models.CharField('Пароль', max_length=254)
    driver = models.CharField('Драйвер', max_length=254)
    title = models.CharField('Отображаемое имя', max_length=254, default='Объект 1')
    get_count_clients = models.BooleanField('Есть зоны', default=False)
    get_total_sum = models.BooleanField('Показывать сумму', default=False)

    def __str__(self):
        return self.database


class FinanceReportCategory(models.Model):
    """Категории финансового отчета"""
    class Meta:
        verbose_name = 'категорию финансового отчета'
        verbose_name_plural = 'Категории финансового отчета'

    title = models.CharField('Имя категории', max_length=254)

    def __str__(self):
        return self.title


class PayAgentReportCategory(models.Model):
    """Категории отчета платежного агента"""

    class Meta:
        verbose_name = 'категорию отчета платежного агента'
        verbose_name_plural = 'Категории отчета платежного агента'

    title = models.CharField('Имя категории', max_length=254)

    def __str__(self):
        return self.title


class TariffList(models.Model):
    """Список имен тарифов"""

    class Meta:
        verbose_name = 'тариф'
        verbose_name_plural = 'Список тарифов'

    title = models.CharField('Тариф', max_length=254)
    finance_report_category = models.ForeignKey(
        FinanceReportCategory,
        verbose_name='Категория финансового отчета',
        on_delete=models.SET_NULL,
        null=True,
    )
    pay_agent_report_category = models.ForeignKey(
        PayAgentReportCategory,
        verbose_name='Категория отчета платежного агента',
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return self.title





# finreport_xls = False
# finreport_google = True
# finreport_telegram = False
# agentreport_xls = False
# split_by_days = True
# date_switch = True
# use_yadisk = False
# check_client_count_total_xls = False
# check_cashreport_xls = False
# check_itogreport_xls = False

# driver = {SQL Server}
# server = 192.168.1.1\SKISRV
# user = sa
# pwd = datakrat
# database1 = Aquapark_Ulyanovsk
# database2 = Beach
# database_bitrix = bitrix_transaction


# [PATH]
# reportxml = data/org_for_report.xml
# agentxml = data/org_plat_agent.xml
# itogreportxml = data/group_for_itogreport.xml

# list_google_docs = data/list_google_docs.csv

