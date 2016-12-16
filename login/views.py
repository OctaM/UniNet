from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from login.forms import UserLoginForm


def login(request):
    return render(request, "login/login.html", {})

def loginUser(request, success_url=None):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            return HttpResponse("Am ajuns cu bine aici")
            user = auth.authenticate(email=request.POST.get('username'),
                                    password=request.POST.get('password'))
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                if success_url:
                    return redirect(reverse(success_url))
                else:
                    return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    #return HttpResponse("Am ajuns cu bine aici")
    return render(request, 'login/login.html', args)
