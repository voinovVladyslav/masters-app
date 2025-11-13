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
