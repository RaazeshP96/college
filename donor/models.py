from django.db import models
from django.contrib.auth.models import User


class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    dob = models.DateField()
    blood_group_list = (
        ('A +ve', 'A +ve'),
        ('B +ve', 'B +ve'),
        ('AB +ve', 'AB +ve'),
        ('O +ve', 'O +ve'),
        ('A -ve', 'A -ve'),
        ('B -ve', 'B -ve'),
        ('AB -ve', 'AB -ve'),
        ('O -ve', 'O -ve'),
    )
    gender_list = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=6, choices=gender_list, default='Male')
    blood_group = models.CharField(max_length=7, choices=blood_group_list, default='A +ve')
    contact_no = models.CharField(max_length=10)
    img = models.ImageField(default='')

    def __str__(self):
        return self.name


class Event(models.Model):
    event_name = models.CharField(max_length=30)
    event_address = models.CharField(max_length=50)
    event_date = models.DateField()
    organised_by = models.CharField(max_length=30)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.event_name




