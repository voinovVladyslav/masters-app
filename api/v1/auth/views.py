from rest_framework.authtoken.views import ObtainAuthToken

from api.v1.auth.serializers import ObtainTokenSerializer


class ObtainTokenApi(ObtainAuthToken):
    serializer_class = ObtainTokenSerializer
