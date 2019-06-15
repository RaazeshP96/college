from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/donor/', {'user': uname})
        else:
            return render(request, 'login.html', {'error': "User not exist"})
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        uname = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            if User.objects.filter(username=uname).exists():
                return render(request, 'register.html', {'error': "Uname already taken"})
            elif User.objects.filter(email=email):
                return render(request, 'register.html', {'error': "Email already taken"})
            else:
                user = User.objects.create_user(first_name=fname, last_name=lname, email=email, username=uname, password=pass1)
                user.save()
                return redirect('/account/login')
        else:
            return render(request, 'register.html', {'error': "Password mismatched"})
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/donor')

