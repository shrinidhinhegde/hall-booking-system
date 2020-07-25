from django.db import models


# Create your models here.
class Booking(models.Model):
    hall1 = models.BooleanField(default=False)
    hall2 = models.BooleanField(default=False)
    date = models.DateField()
    ftime = models.TimeField()
    ttime = models.TimeField()
    purpose = models.CharField(max_length=100)
    approval = models.BooleanField(default = False)
