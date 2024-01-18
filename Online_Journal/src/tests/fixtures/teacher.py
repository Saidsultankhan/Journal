import pytest
from rest_framework.test import APIClient

api_client = APIClient()


def auth_client(user):
    client = APIClient(headers={"Authorization": f"Token {user['token']}"})

    return {"client": client, "user": user["user"]}


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


@pytest.fixture()
def teacher_client(teacher_login):
    return auth_client(teacher_login)


@pytest.mark.django_db
@pytest.fixture
def teacher_create(teacher_factory):
    teacher = teacher_factory.create()

    return teacher


@pytest.mark.django_db
@pytest.fixture
def teachers_list(teacher_factory):
    teachers = teacher_factory.create_batch(3)

    return teachers


@pytest.mark.django_db
@pytest.fixture
def teacher_create_for_dairy(teacher_factory, user_create):
    teacher = teacher_factory.create(user=user_create)

    return teacher
