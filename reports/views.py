from django.http import JsonResponse
from django.views.generic import View

from reports.requests import PeoplesInZoneReport, AllCompanyReport, TotalReport, ClientCountReport
from settings.models import DataBases
from django.db.models import ObjectDoesNotExist
from django.conf import settings


class BaseView(View):
    def __init__(self):
        super(BaseView, self).__init__()
        self.params = None
        self.database = None

    @staticmethod
    def get_params(request):
        params = request.GET
        if not params:
            return None
        return params

    @staticmethod
    def get_database(params):
        database_id = params.get(settings.GET_PARAM_DB)
        if not database_id:
            return None
        try:
            database = DataBases.objects.get(id=database_id)
        except ObjectDoesNotExist:
            return None
        return database

    def get(self, request):
        self.params = self.get_params(request)
        if not self.params:
            return JsonResponse({})
        self.database = self.get_database(self.params)
        if not self.database:
            return JsonResponse({})
        return JsonResponse({})


class PeoplesInZoneView(BaseView):
    def get(self, request):
        super(PeoplesInZoneView, self).get(request)
        peoples_aqua = PeoplesInZoneReport(self.database)
        return JsonResponse(peoples_aqua.query())


class AllCompanyView(BaseView):
    def get(self, request):
        super(AllCompanyView, self).get(request)
        all_company = AllCompanyReport(self.database)
        return JsonResponse(all_company.query())


class TotalView(BaseView):
    def get(self, request):
        super(TotalView, self).get(request)
        date_from = self.params.get('date_from')
        date_to = self.params.get('date_to')
        hide_zero = self.params.get('hide_zero')
        hide_internal = self.params.get('hide_internal')
        total_report = TotalReport(self.database, date_from, date_to, hide_zero, hide_internal)
        return JsonResponse(total_report.query())


class ClientCountView(BaseView):
    def get(self, request):
        super(ClientCountView, self).get(request)
        date_from = self.params.get('date_from')
        date_to = self.params.get('date_to')
        client_count_report = ClientCountReport(self.database, date_from, date_to)
        return JsonResponse(client_count_report.query())
