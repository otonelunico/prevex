from django.conf.urls import url, include
from apps.home.views import index, Verify
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
    url(r'^zohoverify/verifyforzoho.html$', Verify, name="verifyforzoho"),
]