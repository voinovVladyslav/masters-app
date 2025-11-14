from rest_framework import serializers

from materials.models import Material


class MaterialDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = (
            'id',
            'theme',
            'name',
            'order',
            'file',
        )
