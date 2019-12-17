# Generated by Django 2.0.5 on 2019-11-30 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start', models.CharField(max_length=50, null=True)),
                ('Stop', models.CharField(max_length=50, null=True)),
                ('Vehicle_No', models.CharField(max_length=10, null=True)),
                ('Current_Location', models.CharField(max_length=50, null=True)),
                ('Distance', models.CharField(max_length=50, null=True)),
                ('Duration', models.CharField(max_length=50, null=True)),
                ('Complete_Incomplete', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
