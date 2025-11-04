from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from core.models import TimeStampedModel


class UserRole(models.TextChoices):
    STUDENT = "student", "student"
    TEACHER = "teacher", "teacher"
    ADMIN = "admin", "admin"


class UserManager(BaseUserManager):
    def create_user(
        self, email: str, password: str | None = None, **extra_fields
    ) -> "User":
        user: User = self.model(
            email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.full_clean()
        user.save()
        user.refresh_from_db()
        return user

    def create_superuser(
        self, email: str, password: str | None = None, **extra_fields
    ) -> "User":
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(TimeStampedModel, AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(blank=True, default="")
    last_name = models.CharField(blank=True, default="")
    middle_name = models.CharField(blank=True, default="")
    is_active = models.BooleanField(default=True)

    role = models.CharField(
        choices=UserRole.choices,
        max_length=10,
        default=UserRole.STUDENT,
    )

    USERNAME_FIELD = "email"
