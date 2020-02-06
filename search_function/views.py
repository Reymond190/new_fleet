from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from vehicles.models import vehicle
# from app_auth.models import AddDevice
from datetime import date
import json
from app_auth.views import get_temp,get_dataframe,listfun
from pandas.io.json import json_normalize
from requests.auth import HTTPBasicAuth
from django.http import JsonResponse
import requests
class search_listview(ListView):
    queryset = vehicle.objects.all()
    template_name = 'main/class.html'
    model = vehicle


    def get_queryset(self,*args,**kwargs):
        object_list = self.model.objects.all()
        return object_list

def searchlistview(request,*args,**kwargs):
    temp = get_temp()
    y1 = json.loads(temp)
    one = 0
    df1 = get_dataframe(y1)
    df11 = None
    # if request.is_ajax():
    #     x=se(request)
    if request.method == 'GET' and 'viewbutton1' in request.GET:
        plate = request.GET['viewbutton1']
        print(plate)
        p1, v1 = listfun(plate, df1)
    else:
        print('escaped if case on geofence!!!!')
        v1 = "{lat: 28.7041, lng: 77.1025}"
    today = date.today()
    q = request.GET.get('q')
    if q == "today" or q =="Today":
        q = today
    print(q)
    if q is not None:
        queryset =vehicle.objects.filter(Q(name__icontains=q) |Q(plateNumber__icontains=q) |Q(engine__icontains=q) |Q(status__icontains=q) |Q(location__contains=q)).distinct()
        object_list = vehicle.objects.filter(
        )
    else:
        queryset = vehicle.objects.all()
        print('all')
    context = {
        'object_list' : queryset, "plate":v1
    }
    return render(request,"search/view.html",context)

def se(request):
    vehicle1 = request.GET['vehicleno']
    print(vehicle1)
    r1 = requests.get('http://13.235.62.229/location/')
    x1 = r1.json()
    x2 = json.dumps(x1)
    y1 = json.loads(x2)
    df11 = json_normalize(y1)
    print(df11)
    lati =df11['latitude']
    long = df11['longitude']
    data = {
        'lat':float(lati),'long':float(long)
    }



    return JsonResponse(data)