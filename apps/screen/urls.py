from django.conf.urls import url, include
from apps.screen.views import index, Settings, Prevent_, Video_

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^settings/$', Settings, name="settings"),
    url(r'^prevent/(?P<funct>\w+)/(?P<type>\d+)/(?P<id>\d+)$', Prevent_, name="prevent"),
    url(r'^video/(?P<funct>\w+)/(?P<type>\d+)$', Video_, name="video"),
]