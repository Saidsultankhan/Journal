import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
@pytest.fixture
def user_create(user_factory):
    user = user_factory.create()
    user.set_password(user_factory.password)
    user.save()

    return user


@pytest.mark.django_db
@pytest.fixture
def users_list(user_factory):
    user = user_factory.create_batch(3)

    return user


@pytest.mark.django_db
@pytest.fixture
def user_for_teacher_create(user_factory):
    user = user_factory.create()
    user.set_password(user_factory.password)
    user.save()

    return user


@pytest.mark.django_db
@pytest.fixture
def user_for_parent_create(user_factory):
    user = user_factory.create()
    user.set_password(user_factory.password)
    user.save()

    return user


@pytest.mark.django_db
@pytest.fixture
def user_for_pupil_create(user_factory):
    user = user_factory.create()
    user.set_password(user_factory.password)
    user.save()

    return user
