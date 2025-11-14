from django.db.models import Prefetch, QuerySet

from courses.models import Course, Theme
from materials.models import Material


def courses_prefetch_all() -> QuerySet[Course]:
    return Course.objects.select_related('owner').prefetch_related(
        'students',
        Prefetch('themes', queryset=Theme.objects.order_by('order')),
        Prefetch(
            'themes__materials', queryset=Material.objects.order_by('order')
        ),
    )
