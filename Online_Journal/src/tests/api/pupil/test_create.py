import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 201, "SUCCESS"),
        ('admin_client', 400, "BAD_REQUEST"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_pupil_create(
        request,
        client,
        status_code,
        payload,
        user_create,
        grade_create,
        parent_create,
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    statuses = ['FORBIDDEN', 'BAD_REQUEST', 'SUCCESS', 'UNAUTHORIZED']

    datas = {}

    for status in statuses:
        datas[status] = {
            'name_uz': 'Sultan',
            'name_en': 'Sultan',
            'name_ru': 'Sultan',
            'user': user_create.id,
            'grade': grade_create.id,
            'parent': parent_create.id,
        }

        if status == 'BAD_REQUEST':
            datas[status]['parent'] = 1000

    response = auth_client.post(f'/api/v1/pupil_create/', datas[payload])

    if payload == 'SUCCESS':
        assert response.data['name_uz'] == 'Sultan'
        assert response.data['name_en'] == 'Sultan'
        assert response.data['name_ru'] == 'Sultan'
        assert response.data['user'] == user_create.id
        assert response.data['grade'] == grade_create.id
        assert response.data['parent'] == parent_create.id

    assert response.status_code == status_code

