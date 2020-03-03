import json

import requests
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from pandas.io.json import json_normalize

from auth1.settings import API_REPORTS


def advance(request):
    return render(request,"main/advanced.html")


def se(request):
    r1 = requests.get(API_REPORTS)
    x1 = r1.json()
    x2 = json.dumps(x1)
    y1 = json.loads(x2)
    df11 = json_normalize(y1)
    lati =df11['latitude']
    long = df11['longitude']
    imei = df11['device_imei']
    data = x1
    print(data)
    print(type(data))

    return JsonResponse(data,safe=False)