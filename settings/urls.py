from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from .views import settings,v2



urlpatterns = [
    path("settings/",settings,name = 'settings'),
    path("v2/",v2,name = 'v2'),
]