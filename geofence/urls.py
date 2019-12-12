from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
# from app_auth.views import device_listview,devicelistview
from .views import geo,g1

urlpatterns = [
    path('geo/',geo, name='geo'),
    path('g1/',g1, name='g1')
]