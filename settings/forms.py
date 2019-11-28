from django import forms
from .models import Profile

class AddDeviceform(forms.ModelForm):
    class Meta:
        model = AddDevice
        fields = ['Driver_Name','Vehicle_Number','Sim_Number','IMEI_Number',
                  'Device_Model','Vehicle_Licence_No']
