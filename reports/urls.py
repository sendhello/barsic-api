"""barsic_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include

from reports.views import PeoplesInZoneView, AllCompanyView, TotalView, ClientCountView

urlpatterns = [
    path('people-in-zone/', PeoplesInZoneView.as_view(), name='people-in-zone'),
    path('all-company/', AllCompanyView.as_view(), name='all_company'),
    path('total/', TotalView.as_view(), name='total'),
    path('client-count/', ClientCountView.as_view(), name='client-count'),
]
