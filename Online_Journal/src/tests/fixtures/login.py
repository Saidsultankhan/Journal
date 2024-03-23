import pytest
from .auth import *
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
@pytest.fixture
def user_login(user_create):
    data = {
        'username': user_create.username,
        'password': '23456789',
    }
    response = api_client.post('/auth/jwt/create/', data)
    datas = {
        'access': response.data['access'],
        'refresh': response.data['refresh'],
    }

    return datas


@pytest.mark.django_db
@pytest.fixture
def user_role_login(user_create):
    data = {
        'username': user_create.username,
        'password': '23456789',
    }
    response = api_client.post('/auth/token/login/', data)

    datas = {
        "token": response.json()["auth_token"],
        "user": user_create
    }

    return datas


@pytest.mark.django_db
@pytest.fixture
def admin_role_login(admin_create):
    data = {
        'username': admin_create.username,
        'password': '23456789',
    }

    response = api_client.post('/auth/token/login/', data)

    datas = {
        "token": response.json()["auth_token"],
        "user": admin_create
    }

    return datas


@pytest.mark.django_db
@pytest.fixture
def teacher_login(teacher_create_for_dairy):
    data = {
        'username': teacher_create_for_dairy.user.username,
        'password': "23456789",
    }
    response = api_client.post('/auth/token/login/', data)

    data = {
        "token": response.json()["auth_token"],
        "user": teacher_create_for_dairy
    }
    return data


@pytest.mark.django_db
@pytest.fixture
def parent_login(parent_create_to_login):
    data = {
        'username': parent_create_to_login.user.username,
        'password': "23456789",
    }

    response = api_client.post('/auth/token/login/', data)

    data = {
        "token": response.json()["auth_token"],
        "user": parent_create_to_login
    }

    return data


@pytest.mark.django_db
@pytest.fixture
def pupil_login(pupil_create):
    data = {
        'username': pupil_create.user.username,
        'password': "23456789",
    }
    response = api_client.post('/auth/token/login/', data)

    data = {
        "token": response.json()["auth_token"],
        "user": pupil_create
    }

    return data
