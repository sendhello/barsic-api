from abc import ABC, abstractmethod
from typing import Optional, List

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api.reports import (
    PeopleInZone, Companies, TotalReport, ClientCountReport, CashReport, ServicePointsReport, BitrixReport,
    FinanceReport
)
from .serializers import (
    PeopleInZoneSerializer, CompanySerializer, TotalReportSerializer, CashReportSerializer,
    ServicePointsReportSerializer, ClientCountReportSerializer, BitrixReportSerializer, FinanceReportSerializer
)
import re


class BaseViewSet(ViewSet, ABC):
    def __init__(self, *args, **kwargs):
        super(BaseViewSet, self).__init__(*args, **kwargs)
        self.db_type: Optional[str] = None
        self.company_id: Optional[str] = None
        self.date_from: Optional[str] = None
        self.date_to: Optional[str] = None
        self.hide_zero: Optional[str] = None
        self.hide_internal: Optional[str] = None
        self.errors: List[str] = []
        self.allowed_request_params = ['db_type']
        self.required_request_params = ['db_type']

    @abstractmethod
    def list(self, request):
        self.db_type = request.GET.get('db_type', None)
        self.company_id = request.GET.get('company_id', None)
        self.date_from = request.GET.get('date_from', None)
        self.date_to = request.GET.get('date_to', None)
        self.hide_zero = request.GET.get('hide_zero', None)
        self.hide_internal = request.GET.get('hide_internal', None)

        for request_param in self.required_request_params:
            if request_param not in request.GET.keys():
                self.errors.append(f'Не указан обязательный параметр {request_param}')
        for request_param in request.GET.keys():
            if request_param not in self.allowed_request_params:
                self.errors.append(f'Параметр {request_param} не является разрешенным для данного запроса')

        for date in [self.date_from, self.date_to]:
            if date and not re.match(r'\d{4}-\d{2}-\d{2}', date):
                self.errors.append(f'Неверный формат даты {date}. Введите дату в формате "YYYY-MM-DD"')

    def raise_error(self):
        return Response({'status': 'error', 'errors': self.errors, 'data': None})


class PeopleInZoneView(BaseViewSet):
    def list(self, request):
        super(PeopleInZoneView, self).list(request)
        if self.errors:
            return self.raise_error()

        report = PeopleInZone(db_type=self.db_type).query()
        serializer = PeopleInZoneSerializer(report)
        return Response(serializer.data)


class CompanyView(BaseViewSet):
    def list(self, request):
        super(CompanyView, self).list(request)
        if self.errors:
            return self.raise_error()

        report = Companies(self.db_type).query()
        serializer = CompanySerializer(report)
        return Response(serializer.data)


class TotalReportView(BaseViewSet):
    def __init__(self, *args, **kwargs):
        super(TotalReportView, self).__init__(*args, **kwargs)
        self.allowed_request_params.extend(['company_id', 'date_from', 'date_to', 'hide_zero', 'hide_internal'])
        self.required_request_params.append('company_id')

    def list(self, request):
        super(TotalReportView, self).list(request)
        if self.errors:
            return self.raise_error()

        report = TotalReport(
            db_type=self.db_type,
            company_id=self.company_id,
            date_from=self.date_from,
            date_to=self.date_to,
            hide_zero=self.hide_zero,
            hide_internal=self.hide_internal
        ).query()
        serializer = TotalReportSerializer(report)
        return Response(serializer.data)


class TotalReportsView(BaseViewSet):
    def __init__(self, *args, **kwargs):
        super(TotalReportsView, self).__init__(*args, **kwargs)
        self.allowed_request_params.extend(['date_from', 'date_to', 'hide_zero', 'hide_internal'])

    def list(self, request):
        super(TotalReportsView, self).list(request)
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
    def __init__(self, *args, **kwargs):
        super(ClientCountReportView, self).__init__(*args, **kwargs)
        self.allowed_request_params.extend(['company_id', 'date_from', 'date_to'])
        self.required_request_params.append('company_id')

    def list(self, request):
        super(ClientCountReportView, self).list(request)
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
    def __init__(self, *args, **kwargs):
        super(ClientCountReportsView, self).__init__(*args, **kwargs)
        self.allowed_request_params.extend(['date_from', 'date_to'])

    def list(self, request):
        super(ClientCountReportsView, self).list(request)
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
        if self.errors:
            return self.raise_error()

        report = ServicePointsReport(db_type=self.db_type).query()
        serializer = ServicePointsReportSerializer(report)
        return Response(serializer.data)


class CashReportView(BaseViewSet):
    def __init__(self, *args, **kwargs):
        super(CashReportView, self).__init__(*args, **kwargs)
        self.allowed_request_params.extend(['date_from', 'date_to'])

    def list(self, request):
        super(CashReportView, self).list(request)
        if self.errors:
            return self.raise_error()

        report = CashReport(
            db_type=self.db_type,
            date_from=self.date_from,
            date_to=self.date_to
        ).query()
        serializer = CashReportSerializer(report)
        return Response(serializer.data)


class BitrixReportView(BaseViewSet):
    def __init__(self, *args, **kwargs):
        super(BitrixReportView, self).__init__(*args, **kwargs)
        self.allowed_request_params.extend(['date_from', 'date_to'])

    def list(self, request):
        super(BitrixReportView, self).list(request)
        if self.errors:
            return self.raise_error()

        report = BitrixReport(
            db_type=self.db_type,
            date_from=self.date_from,
            date_to=self.date_to
        ).query()
        serializer = BitrixReportSerializer(report)
        return Response(serializer.data)


class FinanceReportView(BaseViewSet):
    def __init__(self, *args, **kwargs):
        super(FinanceReportView, self).__init__(*args, **kwargs)
        self.allowed_request_params = ['date_from', 'date_to']
        self.required_request_params = []

    def list(self, request):
        super(FinanceReportView, self).list(request)
        if self.errors:
            return self.raise_error()

        report = FinanceReport(
            date_from=self.date_from,
            date_to=self.date_to
        ).query()

        serializer = FinanceReportSerializer(report)
        return Response(serializer.data)
