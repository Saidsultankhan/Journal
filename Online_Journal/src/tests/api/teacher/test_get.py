
import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_teacher_get(admin_create, teacher_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    response = api_client.get(f'/api/v1/teacher/{teacher_create.id}/')

    assert response.data['user'] == teacher_create.user.id
