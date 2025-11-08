from django.db import models

from core.models import TimeStampedModel


def material_upload_to(instance: 'Material', filename: str) -> str:
    return 'files/'


class Material(TimeStampedModel):
    name = models.CharField(max_length=200)
    theme = models.ForeignKey(
        'courses.Theme',
        on_delete=models.CASCADE,
        related_name='materials',
    )
    file = models.FileField(upload_to=material_upload_to)
