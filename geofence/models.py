from django.db import models

# Create your models here.
class Geofence(models.Model):
    Area = models.CharField(max_length=50, null=True)
    VehicleNo = models.CharField(max_length=80, null=True)
    Radius = models.CharField(max_length=50, null=True)
    CurrentLocation =models.CharField(max_length=50, null=True)
    Bounds = models.CharField(max_length=50, null=True)
    CenterLocation = models.CharField(max_length=50, null=True)