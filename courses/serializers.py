from rest_framework import serializers
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Course
        fields = '__all__'
