from rest_framework.serializers import Serializer, DictField, CharField, ListField, DateTimeField, BooleanField


class BaseSerializer(Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class RootSerializer(BaseSerializer):
    status = CharField(max_length=64)
    errors = ListField()
    report_type = CharField(max_length=64)


class ReportSerializer(BaseSerializer):
    report = DictField()
    db_name = CharField()


class PeopleInZoneDataSerializer(ReportSerializer):
    pass


class PeopleInZoneSerializer(RootSerializer):
    data = PeopleInZoneDataSerializer()


class CompanyDataSerializer(ReportSerializer):
    pass


class CompanySerializer(RootSerializer):
    data = CompanyDataSerializer()


class TotalReportDataSerializer(ReportSerializer):
    company_name = CharField()
    hide_zero = BooleanField()
    hide_internal = BooleanField()
    date_from = DateTimeField()
    date_to = DateTimeField()


class TotalReportSerializer(RootSerializer):
    data = TotalReportDataSerializer()


class ClientCountReportDataSerializer(ReportSerializer):
    company_name = CharField()
    date_from = DateTimeField()
    date_to = DateTimeField()


class ClientCountReportSerializer(RootSerializer):
    data = ClientCountReportDataSerializer()


class CashReportDataSerializer(ReportSerializer):
    date_from = DateTimeField()
    date_to = DateTimeField()


class CashReportSerializer(RootSerializer):
    data = CashReportDataSerializer()


class ServicePointsReportDataSerializer(ReportSerializer):
    pass


class ServicePointsReportSerializer(RootSerializer):
    data = ServicePointsReportDataSerializer()


# Bitrix
class BitrixReportDataSerializer(ReportSerializer):
    date_from = DateTimeField()
    date_to = DateTimeField()


class BitrixReportSerializer(RootSerializer):
    data = BitrixReportDataSerializer()


class FinanceReportDataSerializer(ReportSerializer):
    date_from = DateTimeField()
    date_to = DateTimeField()


class FinanceReportSerializer(RootSerializer):
    data = FinanceReportDataSerializer()
