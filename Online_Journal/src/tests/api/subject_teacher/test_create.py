import pytest


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
def test_subject_teacher_create(
        request,
        client,
        status_code,
        payload,
        teacher_create,
        subject_create,
        grade_create
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    statuses = ['FORBIDDEN', 'BAD_REQUEST', 'SUCCESS', 'UNAUTHORIZED']

    datas = {}

    for status in statuses:
        datas[status] = {
            'teacher': teacher_create.id,
            'subject': subject_create.id,
            'grade': grade_create.id
        }

        if status == 'BAD_REQUEST':
            datas[status]['grade'] = ''

    response = auth_client.post(f'/api/v1/subject_teacher/create/', datas[payload])
    if payload == 'SUCCESS':
        assert response.data['teacher'] == teacher_create.id

    assert response.status_code == status_code
    