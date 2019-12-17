# Generated by Django 2.0.5 on 2019-11-30 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Driver_Name', models.CharField(max_length=200, null=True)),
                ('Device_Id', models.CharField(max_length=100, null=True)),
                ('Vehicle_Number', models.CharField(max_length=20, null=True)),
                ('Vehicle_Type', models.CharField(choices=[('A', 'Ambulance'), ('M', 'Motorcycle'), ('B', 'Bus'), ('C', 'Car'), ('M', 'Minivan'), ('T', 'Tempo'), ('T', 'Truck')], max_length=20, null=True)),
                ('Sim_Number', models.CharField(max_length=20, null=True)),
                ('IMEI_Number', models.CharField(max_length=20, null=True)),
                ('Device_Model', models.CharField(choices=[('P', 'Prime 07'), ('B', 'Benley 140'), ('O', 'OBDII'), ('R', 'Optimus 2.0')], max_length=20, null=True)),
                ('Vehicle_Licence_No', models.CharField(max_length=10, null=True)),
                ('Device_Timezone', models.CharField(choices=[('UTC-11:00', 'UTC-11:00'), ('UTC-10:00', 'UTC-10:00'), ('UTC-9:00', 'UTC-9:00'), ('UTC-8:00', 'UTC-8:00'), ('UTC-7:00', 'UTC-7:00'), ('UTC-6:00', 'UTC-6:00'), ('UTC-5:00', 'UTC-5:00'), ('UTC-4:00', 'UTC-4:00'), ('UTC-3:00', 'UTC-3:00'), ('UTC-2:00', 'UTC-2:00'), ('UTC-1:00', 'UTC-1:00'), ('UTC+00:00', 'UTC+00:00'), ('UTC+01:00', 'UTC++01:00'), ('UTC+02:00', 'UTC++02:00'), ('UTC+03:00', 'UTC++03:00'), ('UTC+04:00', 'UTC++04:00'), ('UTC+04:30', 'UTC++04:30'), ('UTC+05:00', 'UTC++05:00'), ('UTC+05:30', 'UTC++05:30'), ('UTC+05:45', 'UTC++05:45'), ('UTC+06:00', 'UTC++06:00'), ('UTC+06:30', 'UTC++06:30'), ('UTC+07:00', 'UTC++07:00'), ('UTC+08:00', 'UTC++08:00'), ('UTC+08:30', 'UTC++08:30'), ('UTC+08:45', 'UTC++08:45'), ('UTC+09:00', 'UTC++09:00'), ('UTC+09:30', 'UTC++09:30'), ('UTC+10:00', 'UTC++10:00'), ('UTC+11:00', 'UTC++11:00'), ('UTC+12:00', 'UTC++12:00'), ('UTC+13:00', 'UTC++13:00'), ('UTC+14:00', 'UTC++14:00')], max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]