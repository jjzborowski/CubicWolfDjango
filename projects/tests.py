from django.test import TestCase
from rest_framework.test import requests
from .models import Project


class ProjectTesting(TestCase):
    fixtures = ['fixtures.json']

    # def test_project_name(self):
    #     project = Project.objects.all().first()
    #     expected = project.title
    #     result = str(project)
    #     self.assertEqual(expected, result)

    def test_project_api(self):
        client = RequestsClient()
        expected = Project.objects.all().first()
        result = self.APIRequestFactory().get('/api/projects/1').data
        self.assertEqual(expected, result)
