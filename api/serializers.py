from rest_framework import serializers


class PeopleInZoneDataSerializer(serializers.Serializer):
    report = serializers.DictField()


class PeopleInZoneSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    report_type = serializers.CharField(max_length=64)
    data = PeopleInZoneDataSerializer()


class CompanyDataSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    report = serializers.DictField()


class CompanySerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    report_type = serializers.CharField(max_length=64)
    data = CompanyDataSerializer()


class TotalReportDataSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    company_name = serializers.CharField()
    date_from = serializers.DateTimeField()
    date_to = serializers.DateTimeField()
    hide_zero = serializers.BooleanField()
    hide_internal = serializers.BooleanField()
    report = serializers.DictField()


class TotalReportSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    report_type = serializers.CharField(max_length=64)
    data = TotalReportDataSerializer()


class ClientCountReportDataSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    company_name = serializers.CharField()
    date_from = serializers.DateTimeField()
    date_to = serializers.DateTimeField()
    report = serializers.DictField()


class ClientCountReportSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    report_type = serializers.CharField(max_length=64)
    data = ClientCountReportDataSerializer()


class CashReportDataSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    date_from = serializers.DateTimeField()
    date_to = serializers.DateTimeField()
    report = serializers.DictField()


class CashReportSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    report_type = serializers.CharField(max_length=64)
    data = CashReportDataSerializer()


class ServicePointsReportDataSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    report = serializers.DictField()


class ServicePointsReportSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    report_type = serializers.CharField(max_length=64)
    data = CashReportDataSerializer()
