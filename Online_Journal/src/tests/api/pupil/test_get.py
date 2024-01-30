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
def test_pupil_get(
        request,
        client,
        status_code,
        payload,
        pupil_create
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    if payload == 'NOT_FOUND':
        response = auth_client.get(f'/api/v1/pupil/{pupil_create.id + 1}/')
    else:
        response = auth_client.get(f'/api/v1/pupil/{pupil_create.id}/')

    if payload == 'SUCCESS':
        print(response.data)
        assert response.data['user'] == pupil_create.user.id

    assert response.status_code == status_code
