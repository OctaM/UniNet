from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from .models import News
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def newsfeed(request):
    return render(request, 'newsfeed/index.html')
