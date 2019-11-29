from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from .views import settings



urlpatterns = [
    path("settings/",settings,name = 'settings'),
]