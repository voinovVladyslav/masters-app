from django.contrib import admin

from materials.models import Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        'created_at',
        'name',
        'id',
        'theme',
    )
    raw_id_fields = ('theme',)
