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
def test_subject_teacher_list(
        request,
        client,
        status_code,
        payload,
        subject_teacher_list
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    response = auth_client.get(f'/api/v1/subject_teachers/')

    if payload == 'SUCCESS':
        assert len(response.data) == len(subject_teacher_list)
    else:
        assert response.status_code == status_code
