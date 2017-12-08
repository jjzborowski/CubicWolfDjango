from rest_framework import viewsets
from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework.response import Response


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def test(self, request):
        return Response(request.build_absolute_uri())
