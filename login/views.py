from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from login.forms import UserLoginForm


def login(request):
    return render(request, "login/login.html")


def loginUser(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                return HttpResponse("s-a logat")
            else:
                return HttpResponse("Nu s-a logat")
        else:
            return HttpResponse("Form nu valid")

