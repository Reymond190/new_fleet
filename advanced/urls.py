from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from .views import advance,se



urlpatterns = [
    path("",advance,name = 'advanced'),
    path("ajax/",se,name = 'v2'),
]