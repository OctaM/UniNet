from django.conf.urls import url
from . import views


urlpatterns = [
    # /login/
    url(r'^$', views.loginUser, name='login'),
    url(r'^loginUser/$', views.loginUser, name='loginUser')

]