import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 200, "SUCCESS"),
        ('admin_client', 404, "NOT_FOUND"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_subject_update(
        request,
        client,
        status_code,
        payload,
        subject_create
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    statuses = ['FORBIDDEN', 'NOT_FOUND', 'SUCCESS', 'UNAUTHORIZED']

    datas = {}

    for status in statuses:
        datas[status] = {
            'name_uz': 'Sultan',
            'name_en': 'Subject1',
            'name_ru': 'Subject2',
        }

    if payload == 'NOT_FOUND':
        response = auth_client.patch(f'/api/v1/subject_update/{subject_create.id + 1}/', datas[payload])
    else:
        response = auth_client.patch(f'/api/v1/subject_update/{subject_create.id}/', datas[payload])

    if payload == 'SUCCESS':
        assert response.data['name_uz'] == 'Sultan'

    assert response.status_code == status_code
