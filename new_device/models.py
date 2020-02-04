from django.db import models

# Create your models here.
class AddDevice(models.Model):
    CHOICES_1 = (
        ('Prime 07', 'Prime 07'),
        ('Benley 140', 'Benley 140'),
        ('OBDII', 'OBDII'),
        ('Optimus 2.0', 'Optimus 2.0'),
    )
    CHOICES_2 = (
        ('Ambulance', 'Ambulance'),
        ('Motorcycle', 'Motorcycle'),
        ('Bus', 'Bus'),
        ('Car', 'Car'),
        ('Minivan', 'Minivan'),
        ('Tempo', 'Tempo'),
        ('Truck', 'Truck'),
    )

    CHOICES_3 = (
        ('UTC-11:00', 'UTC-11:00'),
        ('UTC-10:00', 'UTC-10:00'),
        ('UTC-9:00', 'UTC-9:00'),
        ('UTC-8:00', 'UTC-8:00'),
        ('UTC-7:00', 'UTC-7:00'),
        ('UTC-6:00', 'UTC-6:00'),
        ('UTC-5:00', 'UTC-5:00'),
        ('UTC-4:00', 'UTC-4:00'),
        ('UTC-3:00', 'UTC-3:00'),
        ('UTC-2:00', 'UTC-2:00'),
        ('UTC-1:00', 'UTC-1:00'),
        ('UTC+00:00', 'UTC+00:00'),
        ('UTC+01:00', 'UTC++01:00'),
        ('UTC+02:00', 'UTC++02:00'),
        ('UTC+03:00', 'UTC++03:00'),
        ('UTC+04:00', 'UTC++04:00'),
        ('UTC+04:30', 'UTC++04:30'),
        ('UTC+05:00', 'UTC++05:00'),
        ('UTC+05:30', 'UTC++05:30'),
        ('UTC+05:45', 'UTC++05:45'),
        ('UTC+06:00', 'UTC++06:00'),
        ('UTC+06:30', 'UTC++06:30'),
        ('UTC+07:00', 'UTC++07:00'),
        ('UTC+08:00', 'UTC++08:00'),
        ('UTC+08:30', 'UTC++08:30'),
        ('UTC+08:45', 'UTC++08:45'),
        ('UTC+09:00', 'UTC++09:00'),
        ('UTC+09:30', 'UTC++09:30'),
        ('UTC+10:00', 'UTC++10:00'),
        ('UTC+11:00', 'UTC++11:00'),
        ('UTC+12:00', 'UTC++12:00'),
        ('UTC+13:00', 'UTC++13:00'),
        ('UTC+14:00', 'UTC++14:00'),
    )

    Driver_Name = models.CharField(max_length=200,null=True)
    Device_Id = models.CharField(max_length=100,null=True)
    Vehicle_Number = models.CharField(max_length=20,null=True)
    Vehicle_Type = models.CharField(max_length=20,choices=CHOICES_2, null=True)
    Sim_Number = models.CharField(max_length=20,null=True)
    IMEI_Number = models.CharField(max_length=20,null=True)
    Device_Model = models.CharField(max_length=20, choices=CHOICES_1, null=True)
    Vehicle_Licence_No = models.CharField(max_length=10,null=True)
    Device_Timezone = models.CharField(max_length=10,choices=CHOICES_3,null=True)