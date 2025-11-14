from rest_framework import serializers

from api.v1.themes.serializers import ThemeDisplaySerializer
from api.v1.users.serializers import UserDisplaySerializer
from courses.models import Course


class CourseDisplaySerializer(serializers.ModelSerializer):
    owner = UserDisplaySerializer(read_only=True)
    students = UserDisplaySerializer(many=True, read_only=True)
    themes = ThemeDisplaySerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'owner',
            'students',
            'themes',
        )
