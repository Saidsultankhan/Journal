import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.django_db
def test_grade_update(admin_create, grade_create, teacher_create, user_login):
    token = user_login
    api_client.force_authenticate(user=admin_create)
    api_client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
    data = {
        "teacher": teacher_create.id
    }
    response = api_client.patch(f'/api/v1/class_update/{grade_create.id}/', data)

    assert response.data['teacher'] == teacher_create.id
    