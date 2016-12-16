from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^newsfeed/', include('newsfeed.urls')),
    url(r'^$', include('login.urls')),
]
