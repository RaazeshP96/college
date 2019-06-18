from django.contrib import admin
from .models import Donor, Event


class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'address', 'blood_group', 'gender', 'contact_no')


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_date', 'event_address')


admin.site.register(Donor, DonorAdmin)
admin.site.register(Event, EventAdmin)

