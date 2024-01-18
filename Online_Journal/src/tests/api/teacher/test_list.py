
import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_teacher_list(admin_create, teachers_list, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    response = api_client.get(f'/api/v1/teachers/')

    assert len(response.data) == len(teachers_list)
