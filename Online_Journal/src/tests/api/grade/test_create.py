
import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_grade_create(admin_create, teacher_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    data = {
        'type': 'a',
        'number': 11,
        'mentor': teacher_create.id
    }
    response = api_client.post(f'/api/v1/class_create/', data)

    assert response.status_code == 201
