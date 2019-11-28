from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from .views import tickets
from django.conf.urls.static import static


urlpatterns = [
    path("tickets/",tickets,name='tickets'),

    ]