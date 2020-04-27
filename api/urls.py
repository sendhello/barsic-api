from django.urls import path, include

from api.views import PeopleInZoneView, CompanyView, TotalView, ClientCountView
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('people-in-zone/', PeopleInZoneView.as_view({'get': 'retrieve'}), name='people-in-zone'),
#     path('companies/', AllCompanyView.as_view(), name='companies'),
#     path('total/', TotalView.as_view(), name='total'),
#     path('client-count/', ClientCountView.as_view(), name='client-count'),
# ]

router = DefaultRouter()
router.register(r'people-in-zone', PeopleInZoneView, basename='people-in-zone')
router.register(r'companies', CompanyView, basename='companies')
router.register(r'total_report', TotalView, basename='total_report')
urlpatterns = router.urls
