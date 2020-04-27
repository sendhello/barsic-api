from django.contrib import admin
from django.urls import path, include

from api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('api/v1.0/', include(api_urls))
]
