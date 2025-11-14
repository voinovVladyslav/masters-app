from rest_framework import serializers

from api.v1.materials.serializers import MaterialDisplaySerializer
from courses.models import Theme


class ThemeDisplaySerializer(serializers.ModelSerializer):
    materials = MaterialDisplaySerializer(many=True, read_only=True)

    class Meta:
        model = Theme
        fields = (
            'id',
            'course',
            'name',
            'description',
            'order',
            'created_at',
            'materials',
        )
