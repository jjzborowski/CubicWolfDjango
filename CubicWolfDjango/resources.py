from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from projects.models import Project
from courses.models import Course


class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'
        authorization = Authorization()


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        authorization = Authorization()
