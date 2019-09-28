from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from reports.models import DataRequest

from reports.forms import MyForm
from datetime import datetime, timedelta
from reports.requests import sql_query


def test(request):
    if request.method == 'GET':
        return render(request, 'reports/test.html')


class MyView(View):
    def get(self, request):
        form = MyForm()
        c = {
            'form': form,
        }
        return render(request, 'reports/form.html', c)

    def post(self, request):
        form = MyForm(data=request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['message'])
        else:
            messages.error(request, 'Ошибка авторизации')

        c = {'form': form}
        return render(request, 'reports/form.html', c)


class Reports(View):
    def get(self, request):
        r = sql_query()
        return JsonResponse(r)
