from django.conf.urls import url, include
from apps.binnacle.views import index, Create_value, Create_working, Create_accident, All_accident

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^accident/(?P<funct>\w+)/(?P<value>\d+)$', Create_accident, name="accident"),
    url(r'^(?P<value>\w+)/(?P<funct>\w+)/(?P<id>\d+)$', Create_value, name="create_value"),
    url(r'^working/(?P<value>\d+)$', Create_working, name="working"),
    url(r'^all_accident/$', All_accident, name="all_accident"),
    ]