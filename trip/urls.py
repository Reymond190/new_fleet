from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import add_trip,trip

urlpatterns = [
    path('add_trip/', add_trip, name='addtrip'),
    path('trip/', trip, name='trip'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)