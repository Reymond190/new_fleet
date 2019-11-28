from django.db import models

# Create your models here.
class Trip(models.Model):
    start = models.CharField(null = True,max_length=10)
    end = models.CharField(null = True,max_length=10)
    vehicle = models.CharField(null = True,max_length=10)

class AddTrip(models.Model):
  Start = models.CharField(max_length=50, null=True)
  Stop = models.CharField(max_length=50, null=True)
  Vehicle_No = models.CharField(max_length=10, null=True)
  Current_Location = models.CharField(max_length=50, null=True)
  Distance = models.CharField(max_length=50, null=True)
  Duration = models.CharField(max_length=50, null=True)
  Complete_Incomplete = models.CharField(max_length=50, null=True)