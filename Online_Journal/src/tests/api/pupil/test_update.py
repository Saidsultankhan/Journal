import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.django_db
def test_pupil_update(admin_create, pupil_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    data = {
        'name_uz': 'Sultan',
    }
    response = api_client.patch(f'/api/v1/pupil_update/{pupil_create.id}/', data)

    assert response.status_code == 200
