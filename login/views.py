from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, "login/login.html", {})

def userProfile(request, user_id):
    return HttpResponse("<h1> This is the profile with id " + str(user_id) + "</h1>")