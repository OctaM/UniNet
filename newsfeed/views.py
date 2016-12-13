from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from .models import News


def newsfeed(request):
    all_news = News.objects.all()
    context = {
        'all_news' : all_news,
    }
    return render(request, 'newsfeed/index.html', context)

def details(request, news_id):
    try:
        news = News.objects.get(id = news_id)
    except News.DoesNotExist:
        raise Http404("Post does not exist!")
    return render(request, 'newsfeed/details.html', {'news' : news} )