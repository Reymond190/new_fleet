from datetime import datetime

from django.db import models

# Create your models here.
class Helpcenter(models.Model):
    CHOICES_1 = (
        ('App Crashes','App Crashes'),
        ('Feedback','Feedback'),
        ('Problems on live tracking','Problems on live tracking'),
        ('Wrong datas in reports', 'Wrong datas in reports'),
        ('Problems in Graphs', 'Problems in Graphs' ),
        ('Problems in geofence', 'Problems in geofence'),

    )

    no = models.CharField(max_length=50,null=True)
    Title = models.CharField(max_length=50, null=True)
    How_can_we_help_you = models.CharField(max_length=100,choices= CHOICES_1 ,null=True)
    message = models.TextField(max_length=100,null=True)
    comments = models.CharField(max_length=80, null=True)
    time = models.CharField(max_length=80,null=True)


    def save(self):
        self.time = str(datetime.now().date())+","+str(datetime.now().time())
        super(Helpcenter, self).save()