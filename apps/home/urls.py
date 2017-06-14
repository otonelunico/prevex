from django.conf.urls import url, include
from apps.home.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]