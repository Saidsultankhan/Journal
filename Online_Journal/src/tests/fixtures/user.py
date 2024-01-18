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
def users_list(user_factory):
    user = user_factory.create_batch(3)

    return user
