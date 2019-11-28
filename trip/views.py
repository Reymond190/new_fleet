from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import AddTrip
from app_auth.forms import AddTripForm

from app_auth.views import funclu,get_temp,get_dataframe
import json

@csrf_exempt
def add_trip(request):
    print("success")
    temp = get_temp()
    y1 = json.loads(temp)
    df1 = get_dataframe(y1)
    i,j = funclu(df1)
    print(request.method)
    if request.method == 'GET':
            message = "Yes, AJAX!"

    else:
            message = "Not Ajax"
            trip()

    print(message)
    re = AddTrip.objects.all()
    context = {
        "json" : j,
        "message":message,
        "trip": re,
    }

    return render(request, 'trip/add_trip.html',context)

def trip():
    print("save")

    start = request.GET["start"]
    stop = request.GET["end"]
    # startid = request.GET["startid"]
    # endid = request.GET["endid"]
    vehicleno = request.GET["vehicleno"]
    distance = request.GET["distance"]
    duration = request.GET["time"]
    currentlocatio = request.GET["location"]
    currentlocati = request.GET["locations"]
    currentlocation = [currentlocatio,currentlocati]
    queryset = AddTrip()
    queryset.Start = start
    queryset.Stop = stop
    queryset.Vehicle_No = vehicleno
    queryset.Current_Location = currentlocation
    queryset.Distance = distance
    queryset.Duration = duration
    queryset.save()
