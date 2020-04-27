from rest_framework import serializers
from settings.models import DataBase


class PeopleInZoneElementSerializer(serializers.Serializer):
    zone = serializers.CharField()
    people_count = serializers.IntegerField()


class PeopleInZoneDataSerializer(serializers.Serializer):
    zones = PeopleInZoneElementSerializer(many=True)


class PeopleInZoneSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    data = PeopleInZoneDataSerializer()


class CompanyElementSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    address = serializers.CharField()
    inn = serializers.CharField()
    email = serializers.CharField()
    tel = serializers.CharField()
    site = serializers.CharField()


class CompanyDataSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    companies = CompanyElementSerializer(many=True)


class CompanySerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    data = CompanyDataSerializer()


class TotalReportDataSerializer(serializers.Serializer):
    db_name = serializers.CharField()
    company_name = serializers.CharField()
    date_from = serializers.DateTimeField()
    date_to = serializers.DateTimeField()
    hide_zero = serializers.BooleanField()
    hide_internal = serializers.BooleanField()
    total_report = serializers.ListField()


class TotalReportSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=64)
    errors = serializers.ListField()
    data = TotalReportDataSerializer()
