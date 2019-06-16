from django import forms
from .models import Donor


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = [
            'name',
            'address',
            'dob',
            'gender',
            'blood_group',
            'contact_no',
            'img'
        ]
