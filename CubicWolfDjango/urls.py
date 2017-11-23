from django.conf.urls import url, include
from django.contrib import admin
# from .resources import ProjectResource, CourseResource

# project_resource = ProjectResource()
# course_resource = CourseResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('projects.urls')),
    # url(r'^api/', include(course_resource.urls)),
]
