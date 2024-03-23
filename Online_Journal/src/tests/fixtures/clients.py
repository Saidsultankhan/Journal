import pytest
from .auth import *
from django.contrib.auth.models import AnonymousUser


@pytest.fixture
def teacher_client(teacher_login):
    return auth_client(teacher_login)


@pytest.fixture
def parent_client(parent_login):
    return auth_client(parent_login)


@pytest.fixture
def pupil_client(pupil_login):
    return auth_client(pupil_login)


@pytest.fixture
def user_client(user_role_login):
    return auth_client(user_role_login)


@pytest.fixture
def admin_client(admin_role_login):
    return auth_client(admin_role_login)


@pytest.fixture
def un_authorized_client():
    return {"client": APIClient(), "user": AnonymousUser()}


