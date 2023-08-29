from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    about = {'about': "H Financial is a Colombia based web application designed to help you find the simplest way to manage your personal finances."}
    
    return render(request, "home.html", about)

def signup(request):

    if request.method == "POST":

        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname') 
        email = request.POST.get('email')
        password = request.POST.get('password')
        pass2 = request.POST.get('pass2')

        if password == pass2:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname

            user.save()
            messages.success(request, "Your account has been successfully created.")

            return redirect('signin')
        else:
            messages.error(request, "passwords entered are not the same!")
            return redirect('home')        
    
    return render(request, "signup.html")

def signin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name

            return render(request, "index.html", {'fname': fname})
        else:
            messages.error(request, "Bad credentials!")

            return redirect('home')

    return render(request, "signin.html")

def index(request, user):
   
    return render(request, "index.html", {'user': user})

def signout(request):

    logout(request)
    messages.success(request, "Logged out Successfully!")

    return redirect('home')

def goal(request):
    goal = { 'goal': "Buy a house"}

    return render(request, "goal.html", goal)

def settings(request):
    return render(request, "settings.html")
