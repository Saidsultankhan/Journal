import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_teacher_create(user_login, admin_create):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    data = {
        'user': admin_create.id
    }
    response = api_client.post(f'/api/v1/teacher_create/', data)

    assert response.status_code == 201
