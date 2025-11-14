from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.v1.courses.serializers import CourseDisplaySerializer
from api.v1.pagination import DefaultPagination
from courses.services.queryset import courses_prefetch_all


class CourseListApi(ListAPIView):
    serializer_class = CourseDisplaySerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        return courses_prefetch_all()


class CourseDetailApi(RetrieveAPIView):
    serializer_class = CourseDisplaySerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return courses_prefetch_all()
