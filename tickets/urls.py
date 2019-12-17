from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from .views import tickets, username_exists,v1
from django.conf.urls.static import static


urlpatterns = [
    path("tickets/",tickets,name='tickets'),
    path('exists/', username_exists, name='exists'),
    path('v1/', v1, name='v1'),
    ]