from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, ProfileAddForm, AddTripForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
from datetime import datetime
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Profile,Geofence
from django.views.generic import ListView, DetailView
from requests.auth import HTTPBasicAuth

from vehicles.models import vehicle
import json


from background_task import background
import requests
from datetime import timedelta
import datetime
import pandas as pd
import json as simplejson
from pandas.io.json import json_normalize
from django.views.decorators.cache import cache_control


def get_api():
    time2 = datetime.datetime.now()
    time1 = time2 + timedelta(minutes=-5)
    time1 = time1.strftime("%Y-%m-%d %H:%M:00")
    time2 = time2.strftime("%Y-%m-%d %H:%M:00")
    time1 = str(time1)
    time2 = str(time2)
    r1 = requests.get('https://lnt.tracalogic.co/api/ktrack/larsentoubro/' + time1 + '/' + time2,
                      auth=HTTPBasicAuth('admin', 'admin'))
    x1 = r1.json()
    x2 = json.dumps(x1)
    y1 = json.loads(x2)
    return y1

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def profile(request):
    form = ProfileAddForm
    context = {'form':form}
    if request.method == 'POST' and 'button-name1' in request.POST:
        form = ProfileAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile is updated!')
    return render(request,'main/profile.html',context)

def reload_and_store():
    f = open('venv/temp.json', 'w+')
    if f.read() is not None:
        f.truncate(0)
    x = get_api()
    json.dump(x, f)
    f.close()


def get_temp():
    f = open('venv/temp.json', 'r+')
    content = f.read()
    return content


def get_dataframe(y1):
    df1 = json_normalize(y1["assetHistory"])
    df1['serverTimeStamp'] = pd.to_datetime(df1['serverTimeStamp'])
    df1 = df1.set_index('serverTimeStamp')
    df1['eventTimeStamp'] = pd.to_datetime(df1['eventTimeStamp'])  # total no of vehicles
    df1 = df1.drop_duplicates(['deviceImeiNo'],
                              keep='first')  # NUMBER OF VEHICLES WITH UNIQUE DEVICEIMEINO/PLATENUMBER
    return df1


def filter_running(df):
    df2 = df.loc[(df["engine"] == "ON") & (df["speed"] > 0)]  # RUNNING VEHICLES
    return df2


def filter_idle(df):
    df3 = df.loc[(df["engine"] == "ON") & (df["speed"] == 0)]  # IDLE VEHICLES
    return df3


def filter_stop(df):
    df4 = df.loc[(df["engine"] == "OFF") & (df["speed"] == 0)]  # STOP_VEHICLES
    return df4


def myfun1(po):             #argument:dataframe(df)
    lat_list = list(po["latitude"])
    long_list = list(po["longitude"])
    gmaps.configure(api_key="AIzaSyDmXhcX8z4d4GxPxIiklwNvtqxcjZoWsWU")
    fig = gmaps.figure()
    var1 = json.dumps(
        [{'lat': country, 'lng': wins} for country, wins in zip(lat_list, long_list)]
    )
    markers = gmaps.marker_layer(list(zip(lat_list, long_list)))
    fig.add_layer(markers)
    data1 = embed_snippet(views=[fig])
    return data1,var1


def myfunpro(po):             #argument:dataframe(df)
    lat_list = list(po["latitude"])
    long_list = list(po["longitude"])
    # gmaps.configure(api_key="AIzaSyDmXhcX8z4d4GxPxIiklwNvtqxcjZoWsWU")
    # fig = gmaps.figure()
    var1 = json.dumps(
        [{'lat': country, 'lng': wins} for country, wins in zip(lat_list, long_list)]
    )
    return var1


def listfun(plate, df):
    df5 = df.loc[df["plateNumber"] == plate]
    return myfun1(df5)

def listfun2(plate, df):
    df5 = df.loc[df["plateNumber"] == plate]
    return df5

# def get_single_loco(plate,df):
#     df5 = df.loc[df["plateNumber"] == plate]
#     lat_list = list(df5["latitude"])
#     long_list = list(df5["longitude"])
#     p = lat_list[0]
#     q = long_list[0]
#     r = p+q
#     r = str(r)
#     return r


def change_frames(r):  # enter required dataframes in this function
    p1,v1 = myfun1(r)
    listpl = r["plateNumber"]
    listsp = r["speed"]
    listdt = r["eventTimeStamp"].dt.strftime("%Y-%m-%d %I:%M:%S %p")
    result = zip(listpl, listdt, listsp)
    return p1, result

def get_details(r):
    plateno = r["plateNumber"]
    # time = r["serverTimeStamp"]
    speed = r["speed"]
    latitude = r["latitude"]
    longitude = r["longitude"]
    lat = str(latitude)
    log = str(longitude)
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="geoapp")
    location = geolocator.reverse("52.509669, 13.376294")

    engine = r["engine"]
    status = r["status"]

    odometer = r["odometer"]
    assetcode = r["AssetCode"]
    direction = r["direction"]
    result = zip(plateno, speed,engine,status,latitude,longitude,odometer,assetcode,direction,location)
    return result




# ------------------------------------------------------------main-----------------------------------------------------------------------------------

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def start(request):
    return render(request, 'file1.html')

def detail(request):

    queryset = vehicle.objects.all()
    temp = get_temp()
    y1 = json.loads(temp)

    df1 = get_dataframe(y1)
    df2 = filter_running(df1)
    df3 = filter_idle(df1)
    df4 = filter_stop(df1)
    total = len(df1)
    running = len(df2)
    idle = len(df3)
    stop = len(df4)
    if request.method == 'GET' and 'totalbutton' in request.GET:
        p1, result = funclu(df1)
    elif request.method == 'GET' and 'runningbutton' in request.GET:

        p1, result = funclu(df2)
    elif request.method == 'GET' and 'idlebutton' in request.GET:
        p1, result = funclu(df3)
    elif request.method == 'GET' and 'stopbutton' in request.GET:
        p1, result = funclu(df4)
    else:
        p1, result = funclu(df1)

    context = {"object_list":queryset,'total':total,'running':running,'idle':idle, 'stop':stop, "myfile1":result}
    return render(request, 'main/details.html',context)

def advance(request):
    temp = get_temp()
    y1 = json.loads(temp)
    df1 = get_dataframe(y1)
    df2 = filter_running(df1)
    df3 = filter_idle(df1)
    df4 = filter_stop(df1)
    total = len(df1)
    running = len(df2)
    idle = len(df3)
    stop = len(df4)
    queryset = vehicle.objects.all()
    if request.method == 'GET' and 'totalbutton' in request.GET:
        p1, result = funclu(df1)
    elif request.method == 'GET' and 'runningbutton' in request.GET:
        p1, result = funclu(df2)
    elif request.method == 'GET' and 'idlebutton' in request.GET:
        p1, result = funclu(df3)
    elif request.method == 'GET' and 'stopbutton' in request.GET:
        p1, result = funclu(df4)
    else:
        p1, result = funclu(df1)

    context = {
        "myfile": result, 'total': total, 'running': running, 'idle': idle, 'stop': stop, "object_list": queryset
    }
    return render(request,"main/advanced.html",context)



def setting(request):
    return render(request, 'main/../templates/setttings/settings.html')

def helpcenter(request):
    return render(request,'main/helpcenter.html')

def tour(request):
    return render(request,'main/tour.html')

# class devicelistview(ListView):
#     queryset = AddDevice.objects.all()
#     template_name = 'main/class.html'
#
#
#     def get_queryset(self,*args,**kwargs):
#         request = self.request
#         pk = self.kwargs.get('pk')
#         return AddDevice.objects.filter(pk=pk)
#
#
#
# def device_listview(request,pk,*args,**kwargs):
#     queryset = AddDevice.objects.get(pk=pk)
#     instance = AddDevice.objects.get_by_id(pk)
#     #print(instance)
#     # instance = get_object_or_404(AddDevice,id=pk)
#     #print(pk)
#     #print(id)
#     context = {
#         'object_list':queryset
#     }
#     return render(request,"main/class.html",context)



def geofence(request):
    # reload_and_store()
    temp = get_temp()
    y1 = json.loads(temp)
    df1 = get_dataframe(y1)
    df2 = filter_running(df1)
    df3 = filter_idle(df1)
    df4 = filter_stop(df1)
    total = len(df1)
    running = len(df2)
    idle = len(df3)
    stop = len(df4)
    p1, result = funclu(df1)
    queryset = vehicle.objects.all()

    context = {
        "mygeo": result, 'total': total, 'running': running, 'idle': idle, 'stop': stop, "object_list": queryset
    }
    return render(request, 'main/geofence.html', context)

def marker(request):
    return render(request, 'main/marker.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def reports(request):
    # reload_and_store()
    return render(request, 'main/report.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password = password)
            # messages.success(request,f'Your account has been created {username}! Login to continue!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)




# @background(schedule=10)
# def notify_user(pk):
#     idle = pk
#     idle= idle +1
#     return idle


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def map (request):

    # time2 = datetime.datetime.now()
    # time1 = time2 + timedelta(minutes=-5)
    # reload_and_store()

    temp = get_temp()
    y1 = json.loads(temp)
    df1 = get_dataframe(y1)
    df2 = filter_running(df1)
    df3 = filter_idle(df1)
    df4 = filter_stop(df1)



    if request.method == 'GET' and 'totalbutton' in request.GET:
        p1, result = change_frames(df1)
        p1, v1 = myfun1(df1)
    elif request.method == 'GET' and 'runningbutton' in request.GET:
        p1, result = change_frames(df2)
        p1, v1 = myfun1(df2)
    elif request.method == 'GET' and 'idlebutton' in request.GET:
        p1, result = change_frames(df3)
        p1, v1 = myfun1(df3)
    elif request.method == 'GET' and 'stopbutton' in request.GET:
        p1, result = change_frames(df4)
        p1, v1 = myfun1(df4)

    else:
        p1, result = change_frames(df1)
        p1, v1 = myfun1(df1)

    if request.method == 'POST' and 'listbutton' in request.POST:
        plate = request.POST['listbutton']
        p1, v1 = listfun(plate, df1)
        one = listfun2(plate, df1)
        two = get_details(one)
        print(plate)
    else:
        print('escaped if case sorry!!!!')

    total = len(df1)
    running = len(df2)
    idle = len(df3)
    stop = len(df4)
    context = {'myfile':v1,'total':total,'running':running,'idle':idle, 'stop':stop, 'list_plate':result}
    return render(request, 'main/track.html', context)

def funclu(po):
    lat_list = list(po["latitude"])
    long_list = list(po["longitude"])
    v_plate = list(po["plateNumber"])
    #print(len(v_plate))
    data1 = "one"
    v_status = list(po["status"])
    var1 = json.dumps(
        [{'lat': country, 'lng': wins,'plate':num,'status':v_sta} for country, wins, num, v_sta in zip(lat_list, long_list,v_plate,v_status)]
    )
    #print(var1)
    return data1, var1

def cluster(request):
    # reload_and_store()
    temp = get_temp()
    y1 = json.loads(temp)
    df1 = get_dataframe(y1)
    df2 = filter_running(df1)
    df3 = filter_idle(df1)
    df4 = filter_stop(df1)
    total = len(df1)
    running = len(df2)
    idle = len(df3)
    stop = len(df4)
    p1, result = funclu(df1)
    queryset = vehicle.objects.all()

    context = {
        "myfile":result,'total':total,'running':running,'idle':idle, 'stop':stop,"object_list":queryset
    }

    return render(request, 'main/cluster.html',context)

def get_ch(request):
    line = LineData()
    chart = ChartData()
    bar = BarChart()
    print(bar)
    context={"line":line,"chart":chart,"bar":bar}
    return render(request, 'main/chart.html',context)

def LineData():

     r = requests.get('http://13.232.118.209/path')
     x = r.json()
     x1 = json.dumps(x)
     y = json.loads(x1)
     df = json_normalize(y)
     df1 = df.loc[df['current_speed'] < 20]
     df2 = df.loc[(df['current_speed'] >= 20) & (df['current_speed'] <= 40)]
     df3 = df.loc[(df['current_speed'] >= 40) & (df['current_speed'] <= 60)]
     df4 = df.loc[(df['current_speed'] >= 60) & (df['current_speed'] <= 80)]
     df5 = df.loc[(df['current_speed'] >= 80) & (df['current_speed'] <= 100)]
     df6 = df.loc[(df['current_speed'] >= 100) & (df['current_speed'] <= 120)]
     print(df1['current_speed'].count())
     data = {

            "X": [[df1['current_speed'].count()],[df2['current_speed'].count()],[df3['current_speed'].count()],[df4['current_speed'].count()],[df5['current_speed'].count()],[df6['current_speed'].count()]],
            "Y" : [["20"],["21-40"],["41-60"],["61-80"],["81-100"],["101-120"]]
        }
     return data


def ChartData():
    r = requests.get('http://13.232.118.209/api2')
    x = r.json()
    x1 = json.dumps(x)
    y = json.loads(x1)
    df = json_normalize(y)
    to = df["Total"][0]
    ru = df["Running"][0]
    idl = df["Idle"][0]
    st = df["Stop"][0]

    data = {

        "X": [["Total"],["Running"],["Idle"],["Stop"],["NoData"]],
        "Y": [to, ru,idl, st, "0"]
    }
    return data

def BarChart():
    r = requests.get('http://13.232.118.209/path')
    x = r.json()
    x1 = json.dumps(x)
    y = json.loads(x1)
    df = json_normalize(y)
    print(df)
    df1 = df.loc[df['distance'] < 3]
    df2 = df.loc[(df['distance'] >= 4) & (df['distance'] <= 8)]
    df3 = df.loc[(df['distance'] >= 9) & (df['distance'] <= 12)]
    df4 = df.loc[(df['distance'] >= 13) & (df['distance'] <= 20)]
    df5 = df.loc[(df['distance'] >= 21)]
    df6 = df.loc[df['distance'] == 0]
    data = {

        "X": [[df6['distance'].count()],[df1['distance'].count()], [df2['distance'].count()], [df3['distance'].count()],
              [df4['distance'].count()], [df5['distance'].count()]],
        "Y": [["0"], ["5"], ["10"], ["15"], ["20"]]
    }
    return data

class Doughnut(APIView):
        authentication_classes = []
        permission_classes = []
        def get(self, request, format=None):
            r = requests.get(
                ' https://lnt.tracalogic.co/api/ktrack/larsentoubro/2019-08-07 11:00:00/2019-08-07 11:05:00 ',
                auth=HTTPBasicAuth('admin', 'admin'))
            x = r.json()
            x1 = json.dumps(x)
            y = json.loads(x1)
            df = json_normalize(y["assetHistory"])
            df['serverTimeStamp'] = pd.to_datetime(df['serverTimeStamp'])
            df = df.set_index('serverTimeStamp')
            #hello
            df['eventTimeStamp'] = pd.to_datetime(df['eventTimeStamp'])
            df1 = df.drop_duplicates(['deviceImeiNo'], keep='last')
            data = {
                "labels": ["Delhi", "Maharashtra"],
                "data": [len(df1.loc[df1['engine'] == "ON"]), len(df1.loc[df1['engine'] == "OFF"])],
            }
            return Response(data)


class track(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        time2 = datetime.datetime.now()
        time1 = time2 + timedelta(minutes=-5)
        time1 = time1.strftime("%Y-%m-%d %H:%M:00")
        time2 = time2.strftime("%Y-%m-%d %H:%M:00")
        time1 = str(time1)
        time2 = str(time2)
        r = requests.get('https://lnt.tracalogic.co/api/ktrack/larsentoubro/' + time1 + '/' + time2,
                         auth=HTTPBasicAuth('admin', 'admin'))
        x = r.json()
        y = json.loads(x)
        latitudes = []
        longitudes = []
        for i in range(len(y["assetHistory"])):
            latitudes.append(y["assetHistory"][i]["latitude"])
            longitudes.append(y["assetHistory"][i]["longitude"])
        print(len(latitudes))
        print(len(longitudes))
        data = {
            "data": [latitudes, longitudes],
        }
        return Response(data)


def table_map(request):
    return render(request,"main/table_map.html")

def playback(request):
    return render(request,"main/playback.html")
def geo(request):
  area = request.GET['area']
  vno = request.GET['vno']
  return render(request,"main/geofence.html")

