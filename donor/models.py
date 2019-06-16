from django.db import models
from  django.contrib import admin
from django.contrib.auth.models import User


class Donor(models.Model):
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



