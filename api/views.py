from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.reports import PeopleInZone, Companies, TotalReport, ClientCountReport, CashReport, ServicePointsReport
from .serializers import (
    PeopleInZoneSerializer, CompanySerializer, TotalReportSerializer, CashReportSerializer,
    ServicePointsReportSerializer, ClientCountReportSerializer
)

from typing import Optional, List


class BaseViewSet(ViewSet):
    def __init__(self, *args, **kwargs):
        super(BaseViewSet, self).__init__(*args, **kwargs)
        self.db_type: Optional[str] = None
        self.company_id: Optional[str] = None
        self.date_from: Optional[str] = None
        self.date_to: Optional[str] = None
        self.hide_zero: Optional[str] = None
        self.hide_internal: Optional[str] = None
        self.errors: List[str] = []

    def list(self, request):
        self.db_type = request.GET.get('db_type', None)
        self.company_id = request.GET.get('company_id', None)
        self.date_from = request.GET.get('date_from', None)
        self.date_to = request.GET.get('date_to', None)
        self.hide_zero = request.GET.get('hide_zero', None)
        self.hide_internal = request.GET.get('hide_internal', None)

    def raise_error(self):
        return Response({'status': 'error', 'errors': self.errors, 'data': None})


class PeopleInZoneView(BaseViewSet):
    def list(self, request):
        super(PeopleInZoneView, self).list(request)
        if not self.db_type:
            self.errors.append('Не указан обязательный параметр db_type')
        if self.errors:
            return self.raise_error()

        report = PeopleInZone(db_type=self.db_type).query()
        serializer = PeopleInZoneSerializer(report)
        return Response(serializer.data)


class CompanyView(BaseViewSet):
    def list(self, request):
        super(CompanyView, self).list(request)
        if not self.db_type:
            self.errors.append('Не указаны необходимые параметры: db_type')
            return self.raise_error()
        report = Companies(self.db_type).query()
        serializer = CompanySerializer(report)
        return Response(serializer.data)


class TotalReportView(BaseViewSet):
    def list(self, request):
        super(TotalReportView, self).list(request)
        if not self.db_type:
            self.errors.append('Не указан обязательный параметр db_type')
        if not self.company_id:
            self.errors.append('Не указан обязательный параметр company_id')
        if self.errors:
            return self.raise_error()

        report = TotalReport(
            db_type=self.db_type,
            company_id=self.company_id,
            date_from=self.date_from,
            date_to=self.date_to,
            hide_zero=self.ide_zero,
            hide_internal=self.hide_internal
        ).query()
        serializer = TotalReportSerializer(report)
        return Response(serializer.data)


class TotalReportsView(BaseViewSet):
    def list(self, request):
        super(TotalReportsView, self).list(request)
        if not self.db_type:
            self.errors.append('Не указан обязательный параметр db_type')
        if self.errors:
            return self.raise_error()

        companies = Companies(self.db_type).query()

        reports = []
        for company_id in companies.data.report:
            report = TotalReport(
                db_type=self.db_type,
                company_id=company_id,
                date_from=self.date_from,
                date_to=self.date_to,
                hide_zero=self.hide_zero,
                hide_internal=self.hide_internal
            ).query()
            serializer = TotalReportSerializer(report)
            reports.append(serializer.data)
        return Response(reports)


class ClientCountReportView(BaseViewSet):
    def list(self, request):
        super(ClientCountReportView, self).list(request)
        if not self.db_type:
            self.errors.append('Не указан обязательный параметр db_type')
        if not self.company_id:
            self.errors.append('Не указан обязательный параметр company_id')
        if self.errors:
            return self.raise_error()

        report = ClientCountReport(
            db_type=self.db_type,
            company_id=self.company_id,
            date_from=self.date_from,
            date_to=self.date_to
        ).query()
        serializer = ClientCountReportSerializer(report)
        return Response(serializer.data)


class ClientCountReportsView(BaseViewSet):
    def list(self, request):
        super(ClientCountReportsView, self).list(request)
        if not self.db_type:
            self.errors.append('Не указан обязательный параметр db_type')
        if self.errors:
            return self.raise_error()

        companies = Companies(self.db_type).query()

        reports = []
        for company_id in companies.data.report:
            report = ClientCountReport(
                db_type=self.db_type,
                company_id=company_id,
                date_from=self.date_from,
                date_to=self.date_to
            ).query()
            serializer = ClientCountReportSerializer(report)
            reports.append(serializer.data)
        return Response(reports)


class ServicePointsReportView(BaseViewSet):
    def list(self, request):
        super(ServicePointsReportView, self).list(request)
        if not self.db_type:
            self.errors.append('Не указан обязательный параметр db_type')
        if self.errors:
            return self.raise_error()

        report = ServicePointsReport(db_type=self.db_type).query()
        serializer = ServicePointsReportSerializer(report)
        return Response(serializer.data)


class CashReportView(BaseViewSet):
    def list(self, request):
        super(CashReportView, self).list(request)
        if not self.db_type:
            self.errors.append('Не указан обязательный параметр db_type')
        if self.errors:
            return self.raise_error()

        report = CashReport(
            db_type=self.db_type,
            date_from=self.date_from,
            date_to=self.date_to
        ).query()
        serializer = CashReportSerializer(report)
        return Response(serializer.data)
