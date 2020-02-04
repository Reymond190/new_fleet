import json

import requests
from django.shortcuts import render

# Create your views here.
from auth1.settings import API_URL1
from new_device.form import AddDeviceform
from new_device.models import AddDevice


def new_dev(request):
    l = AddDevice.objects.all()
    form = AddDeviceform
    context = {'form2':form,"device_list":l}
    if request.method == 'POST' and 'button-name2' in request.POST:
        form2 = AddDeviceform(request.POST)
        if form2.is_valid():
            Driver_Name = form2.cleaned_data['Driver_Name']
            Device_Id =  form2.cleaned_data['Device_Id']
            Vehicle_Number = form2.cleaned_data['Vehicle_Number']
            Vehicle_Type = form2.cleaned_data['Vehicle_Type']
            Sim_Number = form2.cleaned_data['Sim_Number']
            IMEI_Number = form2.cleaned_data['IMEI_Number']
            Device_Model = form2.cleaned_data['Device_Model']
            Vehicle_Licence_No = form2.cleaned_data['Vehicle_Licence_No']
            Device_Timezone = form2.cleaned_data['Device_Timezone']
            data = {'Driver_Name': Driver_Name, 'Device_Id': Device_Id , 'Vehicle_Number': Vehicle_Number,
                    'Vehicle_Type': Vehicle_Type, 'Sim_Number': Sim_Number, 'IMEI_Number': IMEI_Number, 'Device_Model': Device_Model
                    ,'Vehicle_Licence_No': Vehicle_Licence_No, 'Device_Timezone': Device_Timezone}
            headers = {'Content-type': 'application/json'}
            r = requests.post(API_URL1, data=json.dumps(data), headers=headers)
            print(r.status_code)
    return render(request, 'new_device/new_dev.html', context)