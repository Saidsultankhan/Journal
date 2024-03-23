import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_user_login(user_create):
    data = {
        'username': user_create.username,
        'password': '23456789',
    }
    response = api_client.post('/auth/jwt/create/', data)

    assert response.status_code == 200
