from django.http import JsonResponse
from django.views.generic import View

from reports.requests import PeoplesInZoneReport, AllCompanyReport, TotalReport
from settings.models import DataBases
from django.db.models import ObjectDoesNotExist
from django.conf import settings


def get_params(request):
    params = request.GET
    if not params:
        return None
    return params


def get_database(params):
    database_id = params.get(settings.GET_PARAM_DB)
    if not database_id:
        return None
    try:
        database = DataBases.objects.get(id=database_id)
    except ObjectDoesNotExist:
        return None
    return database


class PeoplesInZoneView(View):
    def get(self, request):
        params = get_params(request)
        if not params:
            return JsonResponse({})
        database = get_database(params)
        if not database:
            return JsonResponse({})
        peoples_aqua = PeoplesInZoneReport(database)
        return JsonResponse(peoples_aqua.query())


class AllCompanyView(View):
    def get(self, request):
        params = get_params(request)
        if not params:
            return JsonResponse({})
        database = get_database(params)
        if not database:
            return JsonResponse({})
        all_company = AllCompanyReport(database)
        return JsonResponse(all_company.query())


class TotalView(View):
    def get(self, request):
        params = get_params(request)
        if not params:
            return JsonResponse({})
        database = get_database(params)
        if not database:
            return JsonResponse({})
        date_from = params.get('date_from')
        date_to = params.get('date_to')
        hide_zero = params.get('hide_zero')
        hide_internal = params.get('hide_internal')
        total_report = TotalReport(database, date_from, date_to, hide_zero, hide_internal)
        return JsonResponse(total_report.query())
