from django.conf.urls import url, include
from apps.inventory.views import index, Create_value, Maintainer_item, Movement_maint, Movement_detail
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(index), name='index'),
    url(r'^movement/(?P<value>\w+)/(?P<code>\d+)/$', login_required(Movement_maint), name='movement'),
    url(r'^movement_detail/(?P<code>\d+)/$', login_required(Movement_detail), name='movement_detail'),
    url(r'^(?P<value>\w+)/create/$', login_required(Create_value), name="create_value"),
    url(r'^item/maintainer/(?P<value>\w+)/(?P<code>\d+)/$', login_required(Maintainer_item), name='maintainer_item'),
]