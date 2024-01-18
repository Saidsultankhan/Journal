import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_teacher_delete(admin_create, teacher_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    response = api_client.delete(f'/api/v1/teacher_delete/{teacher_create.id}/')

    assert response.status_code == 204
    