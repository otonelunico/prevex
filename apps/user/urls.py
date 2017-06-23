from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.user.views import Editaccount,Registeruser, Listuser, Edit_type,Deactivate, Activate

urlpatterns = [
 #   url(r'^$', index, name='ticket'),
    url(r'^register', login_required(Registeruser), name='register'),
    url(r'^list$', login_required(Listuser), name='list'),
    url(r'^deactivate/(?P<id>\d+)/$', login_required(Deactivate), name='deactivate'),
    url(r'^activate/(?P<id>\d+)/$', login_required(Activate), name='activate'),
    url(r'^edit/(?P<id>\d+)$', login_required(Editaccount), name='edit'),
    url(r'^type/(?P<id>\d+)/(?P<type>\w+)/$', login_required(Edit_type), name='edit_type'),
]
