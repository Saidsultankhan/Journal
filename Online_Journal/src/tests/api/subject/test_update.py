import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.django_db
def test_subject_update(admin_create, subject_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    data = {
        'name_uz': 'Sultan',
    }
    response = api_client.patch(f'/api/v1/subject_update/{subject_create.id}/', data)

    assert response.data['name_uz'] == 'Sultan'
