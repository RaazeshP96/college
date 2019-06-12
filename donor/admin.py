from django.contrib import admin
from .models import Donor


class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'address', 'blood_group', 'gender', 'contact_no')


admin.site.register(Donor, DonorAdmin)
