from django.contrib import admin

from courses.models import Course, Theme


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
        'owner',
        'created_at',
    )
    raw_id_fields = (
        'owner',
        'students',
    )


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'order',
        'course',
        'created_at',
    )
    raw_id_fields = ('course',)
