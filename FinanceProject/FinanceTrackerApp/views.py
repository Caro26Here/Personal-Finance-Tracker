from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    about = {'about': "H Financial is a Colombia based web application designed to help you find the simplest way to manage your personal finances."}
    return render(request, "index.html", about)

def signup(request):
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")

def signout(request):
    pass

def goal(request):
    return render(request, "goal.html")

def settings(request):
    return render(request, "settings.html")
