from rest_framework import generics
from projects.models import Project
from CubicWolfDjango.serializers import ProjectSerializer

class ViewProjectsListAPI(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RetrieveProjectAPI(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CreateProjectAPI(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class UpdateProjectAPI(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class DestroyProjectAPI(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
