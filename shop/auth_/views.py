from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

def register(request):
    if request.method == 'GET':
        return render(request , 'register.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username = username , password = password)
        return redirect('home')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('home')
        else:
            error = "username or password incorrect"
            return render(request, 'login.html', {'error': error})
    return render(request , 'login.html')
