import pytest
from rest_framework.test import APIClient

api_client = APIClient()


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 200, "SUCCESS"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_parent_list(
        request,
        client,
        status_code,
        payload,
        admin_create,
        parents_list
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data["client"]

    response = auth_client.get(f'/api/v1/parents/')

    if payload == 'SUCCESS':
        assert len(response.data) == len(parents_list)

    assert response.status_code == status_code
    