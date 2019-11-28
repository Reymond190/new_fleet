from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime

class Profile(models.Model):
    Company_name = models.CharField(max_length=10, default="Amigait technology")
    Company_address = models.CharField(max_length=50, default="Sholinganallur")
    Phone_number = models.CharField(max_length=10, default="9677691904")
    No_of_Vehicles = models.CharField(max_length=3, default="256")
    Active_Devices = models.CharField(max_length=5, default="180")
    Inactive_Devices = models.CharField(max_length=3,default="20")


    #
    # def __str__(self):
    #     return f'{self.user.username} Profile'

class DeviceManager(models.Manager):
    def get_by_id(self,id):
       qs = self.get_queryset().filter(id=id)
       if qs.count() == 1:
         return qs.first()
       return None






class Geofence(models.Model):
    Area = models.CharField(max_length=50, null=True)
    Vehicleno = models.CharField(max_length=80, null=True)
    Radius = models.CharField(max_length=50, null=True)
    PresentLocation =models.CharField(max_length=50, null=True)
    Bounds = models.CharField(max_length=50, null=True)



