
import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.django_db
def test_subject_teacher_update(admin_create, subject_teacher_create, teacher_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    data = {
        'teacher': teacher_create.id
    }
    response = api_client.patch(f'/api/v1/subject_teacher/update/{subject_teacher_create.id}/', data)

    assert response.data['teacher'] == teacher_create.id

