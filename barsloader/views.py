from django.shortcuts import render
from django.views.generic import View

from barsloader.models import Superaccount


class Loader(View):
    def get(self, request):
        id = Superaccount.objects.values('inn').all().first()
        if id:
            return render(request, 'barsloader/test.html', id)
        return render(request, 'barsloader/test.html', {'inn': 'Нет соединения'})
