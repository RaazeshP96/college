from django.shortcuts import render
from django.http import HttpResponse
from .models import Donor, Event
from .form import DonorForm
import datetime


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


def forms(request):
    form = DonorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DonorForm()
    content = {
        'form': form
    }
    return render(request, 'form.html', content)


def events(request):
    event = Event.objects.all()
    ename = event.event_name
    address = event.event_address
    enow = event.event_date - datetime.datetime.now()
    edesc = event.description
    cont = {'ename': ename, 'enow': enow, 'edesc': edesc, 'address': address}
    return render(request, 'base.html', cont)




