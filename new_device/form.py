from django import forms
from .models import AddDevice

class AddDeviceform(forms.ModelForm):
    class Meta:
        model = AddDevice
        fields = '__all__'