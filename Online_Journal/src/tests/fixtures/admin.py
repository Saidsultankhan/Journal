import pytest


@pytest.mark.django_db
@pytest.fixture
def admin_create(user_factory):
    user = user_factory.create()
    user.set_password(user_factory.password)
    user.is_staff = True
    user.save()

    return user
