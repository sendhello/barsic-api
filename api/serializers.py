from rest_framework import serializers


class PeopleInZoneElementSerializer(serializers.Serializer):
    zone = serializers.CharField()
    people_count = serializers.IntegerField()


class PeopleInZoneDataSerializer(serializers.Serializer):
    report = serializers.DictField()


class PeopleInZoneSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    report_type = serializers.CharField(max_length=64)
    data = PeopleInZoneDataSerializer()


class CompanyElementSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    inn = serializers.CharField()
    email = serializers.CharField()
    tel = serializers.CharField()
    site = serializers.CharField()


class CompanyDataSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    report = serializers.DictField(child=CompanyElementSerializer())


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
