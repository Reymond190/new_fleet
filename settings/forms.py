from django import forms
from .models import AddDevice

class AddDeviceform(forms.ModelForm):
    class Meta:
        model = AddDevice
        fields = ['Driver_Name','Device_Id','Vehicle_Number','Vehicle_Type','Sim_Number','IMEI_Number',
                  'Device_Model','Vehicle_Licence_No','Device_Timezone']

