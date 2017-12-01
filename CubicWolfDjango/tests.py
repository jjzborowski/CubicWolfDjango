from django.test import TestCase
import methods


class ProjectTesting(TestCase):
    def test_sum_for_7(self):
        expected = 7
        result = methods.test_sum(3, 4)
        self.assertEqual(expected, result)

    def test_sum_for_10(self):
        expected = 10
        result = methods.test_sum(3, 7)
        self.assertEqual(expected, result)

    def test_sum_for_13(self):
        expected = 13
        result = methods.test_sum(3, 10)
        self.assertEqual(expected, result)
