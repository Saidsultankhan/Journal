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
def test_subject_teacher_delete(
        request,
        client,
        status_code,
        payload,
        subject_teacher_create,
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    if payload == 'NOT_FOUND':
        response = auth_client.delete(f'/api/v1/subject_teacher/delete/{subject_teacher_create.id + 1}/')
    else:
        response = auth_client.delete(f'/api/v1/subject_teacher/delete/{subject_teacher_create.id}/')

    assert response.status_code == status_code
    