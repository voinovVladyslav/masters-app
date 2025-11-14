from django.db import models

from core.models import TimeStampedModel


class Course(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, default='')

    owner = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owned_courses',
    )
    students = models.ManyToManyField(
        'users.User',
        blank=True,
        related_name='courses',
    )


class Theme(TimeStampedModel):
    class Meta:
        unique_together = (('name', 'course'),)

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    order = models.PositiveSmallIntegerField(default=0)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='themes',
    )
