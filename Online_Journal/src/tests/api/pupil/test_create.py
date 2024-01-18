
import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.django_db
def test_pupil_create(admin_create, user_create, grade_create, parent_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    data = {
        'name_uz': 'Sultan',
        'name_en': 'Sultan',
        'name_ru': 'Sultan',
        'user': user_create.id,
        'grade': grade_create.id,
        'parent': parent_create.id,
    }
    response = api_client.post(f'/api/v1/pupil_create/', data)

    assert response.status_code == 201
