import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.django_db
def test_subject_create(admin_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    data = {
        'name_uz': 'Subject',
        'name_en': 'Subject',
        'name_ru': 'Subject',
    }
    response = api_client.post(f'/api/v1/subject_create/', data)

    assert response.status_code == 201
