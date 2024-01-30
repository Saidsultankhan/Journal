import pytest


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 200, "SUCCESS"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_pupil_list(
        request,
        client,
        status_code,
        payload,
        pupils_list
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    response = auth_client.get(f'/api/v1/pupils/')

    if payload == 'SUCCESS':
        assert len(response.data) == len(pupils_list)

    assert response.status_code == status_code
