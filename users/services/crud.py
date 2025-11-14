from typing import Any

from core.services.crud import model_update
from users.models import User, UserRole


def user_create(  # noqa: PLR0913
    *,
    email: str,
    password: str = '',
    first_name: str = '',
    last_name: str = '',
    middle_name: str = '',
    is_staff: bool = False,
    is_superuser: bool = False,
    is_active: bool = True,
    role: UserRole = UserRole.STUDENT,
) -> User:
    user = User(
        email=User.normalize_username(email),
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        is_staff=is_staff,
        is_superuser=is_superuser,
        is_active=is_active,
        role=role,
    )
    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()
    user.full_clean()
    user.save()
    user.refresh_from_db()
    return user


def user_update(
    *,
    user: User,
    **fields: Any,
) -> User:
    password = fields.pop('password', None)
    user, updates = model_update(model=user, **fields)

    if password is not None:
        user.set_password(password)
        user.save(update_fields=['password'])

    return user
