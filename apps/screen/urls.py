from django.conf.urls import url, include
from apps.screen.views import index, Settings, Prevent_, Video_
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^settings/$', login_required(Settings), name="settings"),
    url(r'^prevent/(?P<funct>\w+)/(?P<type>\d+)/(?P<id>\d+)$', login_required(Prevent_), name="prevent"),
    url(r'^video/(?P<funct>\w+)/(?P<type>\d+)$', login_required(Video_), name="video"),
]