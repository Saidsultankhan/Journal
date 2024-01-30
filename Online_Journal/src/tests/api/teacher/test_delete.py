import pytest


@pytest.mark.parametrize(
    'client, status_code, payload',
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('admin_client', 204, "SUCCESS"),
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
        user_create,
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    response = auth_client.delete(f'/api/v1/teacher_delete/{teacher_create.id}/')

    if payload == 'NOT_FOUND':
        response = auth_client.delete(f'/api/v1/teacher_delete/{teacher_create.id + 1}/')

    assert response.status_code == status_code

