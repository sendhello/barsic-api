from django.contrib import admin
from solo.admin import SingletonModelAdmin
from settings.models import SettingBase, SettingBitrix, SettingGoogleSheets, SettingTelegram, SettingYandex, DataBase, \
    FinanceReportCategory, PayAgentReportCategory, Tariff
from django_summernote.admin import SummernoteModelAdmin


class SettingAdmin(SingletonModelAdmin):
    pass


# There is only one item in the table, you can get it this way:
# from .models import SiteConfiguration
# config = SiteConfiguration.objects.get()

# get_solo will create the item if it does not already exist
# config = SiteConfiguration.get_solo()

class TariffListAdmin(SummernoteModelAdmin):
    list_display = ('title', 'finance_report_category', 'pay_agent_report_category')
    list_editable = ('finance_report_category', 'pay_agent_report_category')
    list_filter = ('finance_report_category', 'pay_agent_report_category')
    search_fields = ('title', 'finance_report_category', 'pay_agent_report_category')


class DataBasesAdmin(SummernoteModelAdmin):
    list_display = ('title', 'database', 'server', 'user', 'driver', 'type', 'is_have_zones', 'is_display_sum')


admin.site.register(SettingBitrix, SettingAdmin)
admin.site.register(SettingBase, SettingAdmin)
admin.site.register(SettingYandex, SettingAdmin)
admin.site.register(SettingTelegram, SettingAdmin)
admin.site.register(SettingGoogleSheets, SettingAdmin)
admin.site.register(DataBase, DataBasesAdmin)
admin.site.register(FinanceReportCategory)
admin.site.register(PayAgentReportCategory)
admin.site.register(Tariff, TariffListAdmin)
