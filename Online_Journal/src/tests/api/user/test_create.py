import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_user_create():
    response = api_client.post('/auth/users/', data={
        'email': 'email_test@test.com',
        'username': 'username_1',
        'password': 'password_1',
        }
    )

    assert response.status_code == 201
