import requests
from django.core.serializers import json
from django.shortcuts import render
from pandas.io.json import json_normalize
import json
from googlegeocoder import GoogleGeocoder

from background_task import background
import requests
from datetime import timedelta
import datetime
import pandas as pd
import json as simplejson
from pandas.io.json import json_normalize
from app_auth.forms import GeofenceForm
from .models import Geofence


def geo(request):
  geocoder = GoogleGeocoder("AIzaSyDmXhcX8z4d4GxPxIiklwNvtqxcjZoWsWU")
  area = request.GET['area']
  vno = request.GET['vno']
  lat = request.GET['lats']
  print(lat)
  lng = request.GET['lngs']
  radius = request.GET['radius']
  cl = geocoder.get([lat,lng])

  i = Geofence()
  i.Area= area
  i.VehicleNo = vno
  i.Radius = radius
  i.CurrentLocation = cl[0]
  i.save()
  print("save")
  return render(request,"main/geofence.html")

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
    print(var1)
    return data1, var1


def geofence(request):
    r1 = requests.get(' http://13.232.118.209/path')
    x1 = r1.json()
    x2 = json.dumps(x1)
    y1 = json.loads(x2)
    df1 = json_normalize(y1)
    print(df1)
    p1, result = funclu(df1)
    geoc = Geofence.objects.all()
    context = {
      "mygeo": result,"geocall":geoc,
    }
    return render(request, 'main/geofence.html', context)