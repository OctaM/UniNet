from django.conf.urls import url
from . import views


urlpatterns = [
    # /login/
    url(r'^$', views.login, name='login'),

    #/login/3625
    url(r'^(?P<user_id>[0-9]+)/$', views.userProfile, name='userProfile'),
]