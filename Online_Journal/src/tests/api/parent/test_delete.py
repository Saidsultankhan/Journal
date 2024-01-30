import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 204, "SUCCESS"),
        ('admin_client', 404, "BAD_REQUEST"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_parent_delete(
        request,
        client,
        status_code,
        payload,
        admin_create,
        parent_create
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data["client"]

    if payload == 'BAD_REQUEST':
        response = auth_client.delete(f'/api/v1/parent_delete/{parent_create.id + 1}/')
    else:
        response = auth_client.delete(f'/api/v1/parent_delete/{parent_create.id}/')

    assert response.status_code == status_code
