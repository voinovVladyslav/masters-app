from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    ordering = ('id',)
    search_fields = ('email', 'id')
    list_display = (
        'email',
        'id',
        'first_name',
        'last_name',
        'role',
    )
    list_filter = (
        'role',
        'is_staff',
        'is_active',
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'role')}),
        ('Booleans', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )
    readonly_fields = ('created_at', 'updated_at')
    add_fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
    )
