from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from courses.api import CourseAPI

urlpatterns = format_suffix_patterns([
    url(r'^courses/$', CourseAPI['list']),
    url(r'^courses/(?P<pk>[0-9]+)/$', CourseAPI['detail']),
])
