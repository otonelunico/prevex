from django.conf.urls import url, include
from apps.inventory.views import index, Create_value, Maintainer_item, Movement_maint, Movement_detail

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^movement/(?P<value>\w+)/(?P<code>\d+)/$', Movement_maint, name='movement'),
    url(r'^movement_detail/(?P<code>\d+)/$', Movement_detail, name='movement_detail'),
    url(r'^(?P<value>\w+)/create/$', Create_value, name="create_value"),
    url(r'^item/maintainer/(?P<value>\w+)/(?P<code>\d+)/$', Maintainer_item, name='maintainer_item'),
]