import requests
from django.core.serializers import json
from django.shortcuts import render
from pandas.io.json import json_normalize
import json
from googlegeocoder import GoogleGeocoder
from django.http import JsonResponse
from background_task import background
import requests
from datetime import timedelta
import datetime
import pandas as pd
import json as simplejson
from pandas.io.json import json_normalize
from app_auth.forms import GeofenceForm
from auth1.settings import API_REPORTS
from .models import Geofence


def geo(request):
  geocoder = GoogleGeocoder("AIzaSyDmXhcX8z4d4GxPxIiklwNvtqxcjZoWsWU")
  area = request.GET['area']
  vno = request.GET['vno']
  lat = request.GET['lats']

  lng = request.GET['lngs']
  radius = request.GET['radius']
  cl = geocoder.get([lat,lng])
  bounds = json.loads(request.GET.get('bounds[]'))
  clat = request.GET['centerla']
  clng = request.GET['centerlng']

  if(Geofence.objects.filter(VehicleNo__iexact=vno).exists()):

      data = {

          'Message':'VehicleNo already Exists'

      }

  else:
    i = Geofence()
    i.Area= area
    i.VehicleNo = vno
    i.Radius = radius
    i.CurrentLocation = cl[0]
    i.Bounds = bounds
    i.CenterLocation = clat+','+clng
    i.save()
    print("save")
    data={
        'Message':'Successfully Inserted'
    }
  return JsonResponse(data)


def funclu(po):
    lat_list = list(po["latitude"])
    long_list = list(po["longitude"])
    v_plate = list(po["plateNumber"])
    # print(len(v_plate))
    data1 = "one"
    # v_status = list(po["status"])

    var1 = json.dumps(
      [{'lat': country, 'lng': wins, 'plate': num} for country, wins, num in zip(lat_list, long_list, v_plate)]
    )
    return data1, var1



def geofence(request):
    r1 = requests.get(API_REPORTS)
    x1 = r1.json()
    x2 = json.dumps(x1)
    y1 = json.loads(x2)
    df1 = json_normalize(y1)

    p1, result = funclu(df1)
    geoc = Geofence.objects.all()
    context = {
      "mygeo": result,"geocall":geoc,
    }
    return render(request, 'main/geofence.html', context)

def g1(request):
    i = Geofence()
    veh = request.GET['veh']
    r1 = requests.get(API_REPORTS+veh)
    x1 = r1.json()
    x2 = json.dumps(x1)
    y1 = json.loads(x2)
    df1 = json_normalize(y1)
    p1, result = funclu(df1)

    if(Geofence.objects.filter(VehicleNo__iexact=veh).exists()):
        geof = Geofence.objects.get(VehicleNo=veh)
        p = geof.Bounds
        center = geof.CenterLocation
        radius= geof.Radius


    else:
        s = 'null'
        n = 'null'
        e = 'null'
        w = 'null'

    data = {

          'Currentlocation':geof.CurrentLocation , 'bound':p,'center':center,'cL':result,'Radius':radius

      }
    return JsonResponse(data)