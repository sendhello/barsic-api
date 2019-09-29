from django.http import JsonResponse
from django.views.generic import View

from reports.requests import ReportPeoplesInZone
from settings.models import DataBases
from django.conf import settings


class PeoplesInZone(View):
    def get(self, request):
        database_id = request.GET.get(settings.GET_PARAM_DB)
        if not database_id:
            return JsonResponse({})
        peoples_aqua = ReportPeoplesInZone(DataBases.objects.get(id=database_id))
        return JsonResponse(peoples_aqua.query())
