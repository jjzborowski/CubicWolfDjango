from django.test import TestCase
from courses.models import Course


class CourseTesting(TestCase):
    fixtures = ['fixtures.json']

    def test_course_name(self):
        course = Course.objects.all().first()
        expected = course.title
        result = str(course)
        self.assertEqual(expected, result)
