from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    url(r'^projects/$', views.ViewProjectsListAPI.as_view()),  # GET
    url(r'^projects/c/$', views.CreateProjectAPI.as_view()),  # POST
    url(r'^projects/r/(?P<pk>[0-9]+)/$', views.RetrieveProjectAPI.as_view()),  # GET
    url(r'^projects/u/(?P<pk>[0-9]+)/$', views.UpdateProjectAPI.as_view()),  # PUT
    url(r'^projects/d/(?P<pk>[0-9]+)/$', views.DestroyProjectAPI.as_view()),  # DELETE
]

urlpatterns = format_suffix_patterns(urlpatterns)
