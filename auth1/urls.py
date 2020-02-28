"""auth1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from vehicles import views
from home.views import home

from django.contrib.auth import views as auth_views

from app_auth.views import start, register, profile, track, map,reports,cluster,tour,detail,advance,get_ch,playback

from geofence.views import geofence
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',start,name='index' ),
    # path('class/<int:pk>/',devicelistview.as_view()),
    # path('class-fbv/<int:pk>/', device_listview),
    # path('class/',devicelistview.as_view()),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('reports/',reports,name='reports'),
    path('profile/', profile, name='profile'),
    path('map/', map, name='map'),
    path('chart/', get_ch, name='chart'),
    path('new_dev/', include('new_device.urls')),
    path('adv/', include('advanced.urls')),
    path('track/', track.as_view()),
    path('geofence/', geofence, name='geofence'),

    path('cluster/', cluster, name='cluster'),
    path('playback/', playback, name='playback'),
    path('', include('tickets.urls')),
    path('', include('settings.urls')),
    path('', include('helpcenter.urls')),
    path('geofences/', include('geofence.urls')),
    path('tour/', tour, name='tour'),
    path('search/',include('search_function.urls')),
    path('',include('vehicles.urls')),
    path('',include('alerts.urls')),
    path('detail/',detail,name='detail'),
    path('reports/',include('reports.urls')),
    path('advance/',advance,name='advance'),
    path('', include('trip.urls')),
    path("home/",home,name='home'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)