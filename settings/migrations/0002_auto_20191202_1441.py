# Generated by Django 2.0.5 on 2019-12-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adddevice',
            name='Device_Model',
            field=models.CharField(choices=[('Prime 07', 'Prime 07'), ('Benley 140', 'Benley 140'), ('OBDII', 'OBDII'), ('Optimus 2.0', 'Optimus 2.0')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='adddevice',
            name='Vehicle_Type',
            field=models.CharField(choices=[('Ambulance', 'Ambulance'), ('Motorcycle', 'Motorcycle'), ('Bus', 'Bus'), ('Car', 'Car'), ('Minivan', 'Minivan'), ('Tempo', 'Tempo'), ('Truck', 'Truck')], max_length=20, null=True),
        ),
    ]
