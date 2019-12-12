from django import forms
from .models import Profile
from trip.models import AddTrip
from geofence.models import Geofence
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





class AddTripForm(forms.ModelForm):
    class Meta:
        model = AddTrip
        fields = [ 'Start', 'Stop', 'VehicleNo', 'CurrentLocation', 'Distance', 'Duration', 'Complete_Incomplete']

class GeofenceForm(forms.ModelForm):
    class Meta:
        model = Geofence
        fields = [ 'VehicleNo', 'Area', 'Radius', 'CurrentLocation','Bounds','CenterLocation']