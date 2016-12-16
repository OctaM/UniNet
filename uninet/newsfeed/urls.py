from django.conf.urls import url
from . import views

app_name = 'newsfeed'

urlpatterns = [
    # /newsfeed/
    url(r'^$', views.newsfeed, name='newsfeed'),

    # /newsfeed/312312
    url(r'^(?P<news_id>[0-9]+)/$', views.details, name='details'),
]