# Generated by Django 2.0.5 on 2019-12-02 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_addtrip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtrip',
            old_name='Current_Location',
            new_name='CurrentLocation',
        ),
        migrations.RenameField(
            model_name='addtrip',
            old_name='Vehicle_No',
            new_name='VehicleNo',
        ),
    ]
