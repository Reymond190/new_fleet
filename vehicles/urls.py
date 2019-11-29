from django.urls import path, include
from .views import auto
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from vehicles import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("new/", auto,name='fck')
]
if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)