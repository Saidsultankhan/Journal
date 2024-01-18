
import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.django_db
def test_teacher_update(admin_create, user_create, teacher_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    if teacher_create.user.id != user_create.id:
        data = {
            'user': user_create.id
        }
    else:
        print("The users' ids' are the same")
    response = api_client.patch(f'/api/v1/teacher_update/{teacher_create.id}/', data)

    assert response.data['user'] == user_create.id
