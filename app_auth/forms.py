from django import forms
from .models import Profile, AddDevice, AddTickets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ProfileAddForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Company_name', 'Company_address', 'Phone_number', 'No_of_Vehicles', 'Active_Devices', 'Inactive_Devices']


class AddDeviceform(forms.ModelForm):
    class Meta:
        model = AddDevice
        fields = ['Driver_Name','Vehicle_Number','Sim_Number','IMEI_Number',
                  'Device_Model','Vehicle_Licence_No']

class AddTicketsForm(forms.ModelForm):
    class Meta:
        model = AddTickets
        fields = ['Ticket_Name', 'Description']

class AddTripForm(forms.ModelForm):
    class Meta:
        model = AddTrip
        fields = ['Sno', 'Start', 'Stop', 'Vehicle_No', 'Current_Location', 'Distance', 'Duration', 'Complete_Incomplete']