from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from api.v1.pagination import DefaultPagination
from api.v1.users.serializers import UserCreateSerializer, UserDisplaySerializer
from users.models import User


class UserListApi(ListAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = UserDisplaySerializer
    pagination_class = DefaultPagination


class UserSelfApi(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserDisplaySerializer

    def get_object(self):
        assert self.request.user is not None
        return self.request.user

    def get(self, request: Request) -> Response:
        user = self.get_object()
        return Response(
            UserDisplaySerializer(user).data, status=status.HTTP_200_OK
        )


class UserCreateApi(CreateAPIView):
    input_serializer_class = UserCreateSerializer
    output_serializer_class = UserDisplaySerializer

    @extend_schema(
        request=UserCreateSerializer,
        responses={status.HTTP_201_CREATED: UserDisplaySerializer},
    )
    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid()
        user = serializer.save()
        return Response(
            UserDisplaySerializer(user).data, status=status.HTTP_201_CREATED
        )
