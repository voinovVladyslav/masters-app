from rest_framework.generics import ListAPIView

from api.v1.courses.serializers import CourseDisplaySerializer
from courses.models import Course


class CourseListApi(ListAPIView):
    serializer_class = CourseDisplaySerializer

    def get_queryset(self):
        return Course.objects.select_related('owner').prefetch_related(
            'students',
        )
