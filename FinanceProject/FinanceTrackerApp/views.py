from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    about = {'about': "H Financial is a Colombia based web application designed to help you find the simplest way to manage your personal finances."}
    return render(request, "index.html", about)

def signup(request):

    if request.method == "POST":
        # username = request.POST.get('username') also works.
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        pass2 = request.POST.get('pass2')

        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname

        user.save()
        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')
    
    return render(request, "signup.html")

def signin(request):
    return render(request, "signin.html")

def signout(request):
    pass

def goal(request):
    goal = { 'goal': "Buy a house"}
    return render(request, "goal.html", goal)

def settings(request):
    return render(request, "settings.html")
