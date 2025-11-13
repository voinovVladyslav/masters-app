from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from core.models import TimeStampedModel


class UserRole(models.TextChoices):
    STUDENT = 'student', 'student'
    TEACHER = 'teacher', 'teacher'
    ADMIN = 'admin', 'admin'


class UserManager(BaseUserManager):
    def create_user(
        self, email: str, password: str | None = None, **extra_fields
    ) -> 'User':
        from users.services.crud import user_create

        return user_create(email=email, password=password or '', **extra_fields)

    def create_superuser(
        self, email: str, password: str | None = None, **extra_fields
    ) -> 'User':
        from users.services.crud import user_create

        return user_create(
            email=email,
            password=password or '',
            **extra_fields,
            is_staff=True,
            is_superuser=True,
        )


class User(TimeStampedModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(blank=True, default='')
    last_name = models.CharField(blank=True, default='')
    middle_name = models.CharField(blank=True, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    role = models.CharField(
        choices=UserRole.choices,
        max_length=10,
        default=UserRole.STUDENT,
    )

    USERNAME_FIELD = 'email'
    objects = UserManager()
