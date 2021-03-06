import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pandas.io.json import json_normalize

from auth1.settings import API_REPORTS
from .models import AddTrip
from app_auth.forms import AddTripForm

from app_auth.views import funclu,get_temp,get_dataframe
import json

@csrf_exempt
def add_trip(request):
    r1 = requests.get(API_REPORTS)
    x1 = r1.json()
    x2 = json.dumps(x1)
    y1 = json.loads(x2)
    df1 = json_normalize(y1)
    i,j = funclu(df1)
    print(request.method)
    if request.is_ajax():
            message = "Yes, AJAX!"
            start = request.GET["start"]
            stop = request.GET["end"]
            vehicleno = request.GET["vehicleno"]
            distance = request.GET["distance"]
            duration = request.GET["time"]
            currentlocation1 = request.GET["location1"]
            currentlocation2 = request.GET["location2"]
            currentlocation3 = currentlocation1 +','+ currentlocation2
            queryset = AddTrip()
            queryset.Start = start
            queryset.Stop = stop
            queryset.VehicleNo = vehicleno
            queryset.CurrentLocation = currentlocation3
            queryset.Distance = distance
            queryset.Duration = duration
            queryset.save()
            print("saved")

    else:
            message = "Not Ajax"


    print(message)
    re = AddTrip.objects.all()
    context = {
        "json" : j,
        "message":message,
        "trip": re,
    }

    return render(request, 'trip/add_trip.html',context)





