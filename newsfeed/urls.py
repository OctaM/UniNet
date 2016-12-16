from django.conf.urls import url
from . import views

app_name = 'newsfeed'

urlpatterns = [
    # /newsfeed/
    url(r'^$', views.newsfeed, name='newsfeed'),
]