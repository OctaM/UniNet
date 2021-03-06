from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^newsfeed/', include('newsfeed.urls')),
    url(r'^$', RedirectView.as_view(url='/newsfeed/'))
]
