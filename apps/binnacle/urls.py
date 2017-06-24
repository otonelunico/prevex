from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.binnacle.views import index, Create_value, Create_working, Create_accident, All_accident, All_repose

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^accident/(?P<funct>\w+)/(?P<value>\d+)$', login_required(Create_accident), name="accident"),
    url(r'^(?P<value>\w+)/(?P<funct>\w+)/(?P<id>\d+)$', login_required(Create_value), name="create_value"),
    url(r'^working/(?P<value>\d+)$', login_required(Create_working), name="working"),
    url(r'^all_accident/$', login_required(All_accident), name="all_accident"),
    url(r'^all_repose/$', login_required(All_repose), name="all_repose"),
    ]