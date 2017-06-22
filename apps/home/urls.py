from django.conf.urls import url, include
from apps.home.views import index, Verify

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^zohoverify/verifyforzoho.html$', Verify, name="verifyforzoho"),
]