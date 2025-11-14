from rest_framework import serializers

from courses.models import Theme


class ThemeDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = (
            'id',
            'name',
            'description',
            'order',
            'course',
            'created_at',
        )
