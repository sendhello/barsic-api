from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from reports.models import DataRequest

from reports.forms import MyForm
from datetime import datetime, timedelta


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
        datarequest = DataRequest()
        r = datarequest
        datarequest.request_date = datetime.utcnow()
        datarequest.time_type = 'дневной'
        datarequest.date_from = datetime.utcnow() - timedelta(22)
        datarequest.date_to = datetime.utcnow() - timedelta(20)
        datarequest.data = 'JSON{}'
        datarequest.author = 'I'
        print(datarequest.id)
        print(datarequest.request_date)
        print(datarequest.time_type)
        print(datarequest.date_from)
        print(datarequest.date_to)
        print(datarequest.data)
        print(datarequest.author)
        print(datarequest.all_clients_in_zone())
        print(datarequest.request_base())
        print(datarequest.data)
        datarequest.save()
        print(DataRequest.objects.all())
        return render(request, 'reports/reports.html', {'r': 'ffffff'})
