from django.conf.urls import patterns, url

from mpd_client import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^play/$', views.play, name='play'),
)