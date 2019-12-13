from django.db import models

# Create your models here.

class Alert(models.Model):
    alert_name = models.CharField(null = True,max_length=10)
    vehicle_id = models.CharField(null = True,max_length=10)
    alert_type = models.CharField(null = True,max_length=10)
    priority = models.CharField(null = True,max_length=10)
    contact_no = models.CharField(null = True,max_length=10)
    action = models.CharField(null = True,max_length=10)
    latitude = models.CharField(null = True,max_length=10)
    longitude = models.CharField(null = True,max_length=10)

