import pytest


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
def test_teacher_create(
        request,
        client,
        status_code,
        payload,
        teacher_create,
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    response = auth_client.get(f'/api/v1/teacher/{teacher_create.id}/')

    if payload == 'NOT_FOUND':
        response = auth_client.get(f'/api/v1/teacher/{teacher_create.id + 1}/')

    assert response.status_code == status_code
