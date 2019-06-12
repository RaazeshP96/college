from django.shortcuts import render
from django.http import HttpResponse
from .models import Donor


def index(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')


def donor(request):
    donors = Donor.objects.all()
    return render(request, 'donor.html', {'donors': donors})


def contact(request):
    return render(request, 'contact.html')


def reciever(request):
    return render(request, 'reciever.html')


def donate(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        uname = request.POST['username']
        email = request.POST['Email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
    return render(request, 'account/register.html')