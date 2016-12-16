from django.conf.urls import url
from . import views


urlpatterns = [
    # /login/
    url(r'^$', views.login_view, name='login'),
    url(r'^loginUser/$', views.loginUser, name='loginUser'),
    url(r'^profile/$', views.profile_view, name='profileView'),

]