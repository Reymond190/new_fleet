from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import AddTrip
from app_auth.forms import AddTripForm

from app_auth.views import funclu,get_temp,get_dataframe
import json

@csrf_exempt
def add_trip(request):
    temp = get_temp()
    y1 = json.loads(temp)
    df1 = get_dataframe(y1)
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
            currentlocation3 = [currentlocation1, currentlocation2]
            queryset = AddTrip()
            queryset.Start = start
            queryset.Stop = stop
            queryset.Vehicle_No = vehicleno
            queryset.Current_Location = currentlocation3
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





