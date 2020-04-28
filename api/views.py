from django.http import JsonResponse
from django.views.generic import View

from api.reports import PeopleInZone, Companies, TotalReport, ClientCount
from settings.models import DataBase
from django.db.models import ObjectDoesNotExist
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .serializers import PeopleInZoneSerializer, CompanySerializer, TotalReportSerializer


class BaseViewSet(ViewSet):
    def raise_error(self, errors):
        return Response({'status': 'error', 'errors': errors, 'data': None})


class PeopleInZoneView(BaseViewSet):
    def list(self, request):
        people_in_zone = PeopleInZone().query()
        serializer = PeopleInZoneSerializer(people_in_zone)
        return Response(serializer.data)


class CompanyView(BaseViewSet):
    def list(self, request):
        db_type = request.GET.get('db_type', None)
        if not db_type:
            return self.raise_error('Не указаны необходимые параметры: db_type')
        companies = Companies().query(db_type)
        serializer = CompanySerializer(companies)
        return Response(serializer.data)


class TotalView(BaseViewSet):
    def list(self, request):
        db_type = request.GET.get('db_type', None)
        company_id = request.GET.get('company_id', None)
        date_from = request.GET.get('date_from', None)
        date_to = request.GET.get('date_to', None)
        hide_zero = request.GET.get('hide_zero', None)
        hide_internal = request.GET.get('hide_internal', None)
        errors = []
        if not db_type:
            errors.append('Не указан обязательный параметр db_type')
        if not company_id:
            errors.append('Не указан обязательный параметр company_id')
        if errors:
            return self.raise_error(errors)

        total_report = TotalReport().query(
            db_type=db_type,
            company_id=company_id,
            date_from=date_from,
            date_to=date_to,
            hide_zero=hide_zero,
            hide_internal=hide_internal
        )
        serializer = TotalReportSerializer(total_report)
        return Response(serializer.data)


class ClientCountView(BaseViewSet):
    def get(self, request):
        if not self.check_database(request):
            return JsonResponse({'error': 'Database not found'})
        date_from = self.params.get('date_from')
        date_to = self.params.get('date_to')
        client_count_report = ClientCount(self.database, date_from, date_to)
        return JsonResponse(client_count_report.query())
