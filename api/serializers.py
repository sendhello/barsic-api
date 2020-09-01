from rest_framework.serializers import Serializer, DictField, CharField, ListField, DateTimeField, BooleanField


class BasetSerializer(Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class RootSerializer(BasetSerializer):
    status = CharField(max_length=64)
    errors = ListField()
    report_type = CharField(max_length=64)


class ReportSerializer(BasetSerializer):
    report = DictField()


class DateMixin:
    date_from = DateTimeField()
    date_to = DateTimeField()


class DbNameMixin:
    db_name = CharField()


class PeopleInZoneDataSerializer(ReportSerializer):
    pass


class PeopleInZoneSerializer(RootSerializer):
    data = PeopleInZoneDataSerializer()


class CompanyDataSerializer(ReportSerializer, DbNameMixin):
    pass


class CompanySerializer(RootSerializer):
    data = CompanyDataSerializer()


class TotalReportDataSerializer(ReportSerializer, DbNameMixin, DateMixin):
    company_name = CharField()
    hide_zero = BooleanField()
    hide_internal = BooleanField()


class TotalReportSerializer(RootSerializer):
    data = TotalReportDataSerializer()


class ClientCountReportDataSerializer(ReportSerializer,DbNameMixin, DateMixin):
    company_name = CharField()


class ClientCountReportSerializer(RootSerializer):
    data = ClientCountReportDataSerializer()


class CashReportDataSerializer(ReportSerializer, DbNameMixin, DateMixin):
    pass


class CashReportSerializer(RootSerializer):
    data = CashReportDataSerializer()


class ServicePointsReportDataSerializer(ReportSerializer, DbNameMixin):
    pass


class ServicePointsReportSerializer(RootSerializer):
    data = ServicePointsReportDataSerializer()
