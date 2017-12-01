from rest_framework import viewsets
from courses.models import Course
from courses.serializers import CourseSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
