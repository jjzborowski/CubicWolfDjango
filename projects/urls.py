from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from projects.api import ProjectAPI

urlpatterns = format_suffix_patterns([
    url(r'^projects/$', ProjectAPI['list']),
    url(r'^projects/(?P<pk>[0-9]+)/$', ProjectAPI['detail']),
    url(r'^projects/test/$', ProjectAPI['test']),
])
