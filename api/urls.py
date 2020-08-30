from django.urls import path, include

from api.views import (PeopleInZoneView, CompanyView, TotalReportView, TotalReportsView, ClientCountView,
                       CashReportView, ServicePointsReportView)
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('people-in-zone/', PeopleInZoneView.as_view({'get': 'retrieve'}), name='people-in-zone'),
#     path('companies/', AllCompanyView.as_view(), name='companies'),
#     path('total/', TotalView.as_view(), name='total'),
#     path('client-count/', ClientCountView.as_view(), name='client-count'),
# ]

router = DefaultRouter()
router.register(r'cash-report', CashReportView, basename='cash_report')
router.register(r'companies', CompanyView, basename='companies')
router.register(r'people-in-zone', PeopleInZoneView, basename='people_in_zone')
router.register(r'service-points-report', ServicePointsReportView, basename='service_points_report')
router.register(r'total-report', TotalReportView, basename='total_report')
router.register(r'total-reports', TotalReportsView, basename='total_reports')
urlpatterns = router.urls
