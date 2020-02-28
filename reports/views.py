import requests
from django.shortcuts import render
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from requests.auth import HTTPBasicAuth
from pandas.io.json import json_normalize

from auth1.settings import API_REPORTS
from vehicles.models import vehicle
from datetime import date
import json
from trip.models import AddTrip
from django.template.defaulttags import register
from app_auth.views import get_temp,get_dataframe,listfun


def travel_summary(request):
    queryset = vehicle.objects.all()
    p = get_api()
    print('hello')
    print(type(p))
    context = {"object_list":queryset,'one1':p}
    return render(request, 'reports/travel_summary.html',context)


import datetime



def detail_travel_summary(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/travel_detail_summary.html',context)

def trip_summary(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/trip_summary.html',context)


def stoppage_summary(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/stoppage_summary.html',context)

def idle_summary(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    p1 = get_api()
    print(p)
    context = {"object_list":queryset,'data':p,'one1':p1}
    return render(request, 'reports/idle_summary.html',context)

def idle_detail_summary(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    p1 = get_api()
    print(p)
    context = {"object_list":queryset,'date':p,'one1':p1}
    return render(request, 'reports/idle_detail_summary.html',context)

def inactive_summary(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/inactive_summary.html',context)

def ignition_summary(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/ignition_summary.html',context)

def ac_summary(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    p1=get_api()
    print(p)
    context = {"object_list":queryset,'date':p,'one1':p1}
    return render(request, 'reports/ac_summary.html',context)

def ac_misused_summary(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    p1 = get_api()
    print(p)
    context = {"object_list":queryset,'date':p,'one1':p1}
    return render(request, 'reports/ac_misused_summary.html',context)

def speed_vs_distance(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/speed_vs_distance.html',context)

def vehicle_location(request):

    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    p1 = get_api()
    print(p)
    context = {"object_list":queryset,'date':p,'one1':p1}
    return render(request, 'reports/vehicle_location.html',context)

def sms_email(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/sms_email.html',context)

def vehicle_status(request):
        queryset = vehicle.objects.all()
        x = datetime.datetime.now()
        p1 = get_api()
        p = x.date()
        print(p)
        context = {"object_list": queryset, 'date': p, 'one1': p1}
        return render(request, 'reports/vehicle_status.html', context)

def system_log(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/system_log.html',context)

def device_log(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/device_log.html',context)

def analog_data(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/analog_data.html',context)

def personal_report(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/personal_report.html',context)

def report_generator(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/report_generator.html',context)


def actual_trip_summary(request):
    queryset = AddTrip.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    p1=get_api()
    print(p)
    context = {"object_list":queryset,'date':p,'one1':p1}
    return render(request, 'reports/actual_trip_summary.html',context)

def rfid_data(request):
    queryset = vehicle.objects.all()
    x = datetime.datetime.now()
    p = x.date()
    print(p)
    context = {"object_list":queryset,'date':p}
    return render(request, 'reports/rfid_data.html',context)


def get_api():
    r1 = requests.get(API_REPORTS)
    x1 = r1.json()
    x2 = json.dumps(x1)
    y1 = json.loads(x2)
    x1 = json_normalize(y1)
    p = x1.to_dict()
    print(type(p))
    return p


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary[key]