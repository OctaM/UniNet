from django.http import HttpResponse
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from login.forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from newsfeed import templates


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponse("estideja logat")
    else:
        return render(request, "login/login.html")


def loginUser(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                context = {
                    'username': request.user.get_username()
                }
                return render(request, "newsfeed/index.html")
            else:
                return HttpResponse("Nu s-a logat")
        else:
            return render(request, "login/login_invalid.html")


@login_required(login_url='/login/')
def profile_view(request):
    if request.user.is_authenticated:
        return render(request, "login/index.html")
    else:
        return render(request, "nope")