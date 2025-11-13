from django.contrib.auth import authenticate
from rest_framework import serializers


class ObtainTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        attrs = super().validate(attrs)
        email = attrs['email']
        password = attrs['password']
        user = authenticate(
            request=self.context['request'], email=email, password=password
        )
        if not user:
            raise serializers.ValidationError(
                {'message': 'Invalid credentials'}, code='auth'
            )

        attrs['user'] = user
        return attrs
