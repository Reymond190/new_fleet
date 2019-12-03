from datetime import datetime

from django.db import models

# Create your models here.

class AddTickets(models.Model):
    CHOICES_1 = (
        ('LOW','LOW'),
        ('MEDIUM','MEDIUM'),
        ('HIGH','HIGH'),
    )

    no = models.CharField(max_length=50,null=True)
    Ticket_Name = models.CharField(max_length=50, null=True)
    priority = models.CharField(max_length=100,choices= CHOICES_1 ,null=True)
    Description = models.TextField(max_length=80, null=True)
    time = models.CharField(max_length=80,null=True)


    def save(self):
        self.time = str(datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        super(AddTickets, self).save()
