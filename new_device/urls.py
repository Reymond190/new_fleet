from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import new_dev, se

urlpatterns = [
    path('', new_dev, name='new_dev'),
    path('ajax/',se,name='se')
]