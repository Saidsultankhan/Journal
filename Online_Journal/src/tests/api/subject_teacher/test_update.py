
import pytest
from rest_framework.test import APIClient


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
def test_subject_teacher_update(
        request,
        client,
        status_code,
        payload,
        subject_teacher_create,
        teacher_create,
        subject_create,
        grade_create
):
    auth_client_data = request.getfixturevalue(client)
    auth_client = auth_client_data['client']

    statuses = ['FORBIDDEN', 'NOT_FOUND', 'SUCCESS', 'UNAUTHORIZED']

    datas = {}

    for status in statuses:
        datas[status] = {
            'teacher': teacher_create.id,
            'subject': subject_create.id,
            'grade': grade_create.id
        }

    response = auth_client.patch(f'/api/v1/subject_teacher/update/{subject_teacher_create.id}/', datas[payload])

    if payload == 'NOT_FOUND':
        response = auth_client.patch(f'/api/v1/subject_teacher/update/{subject_teacher_create.id + 1}/', datas[payload])

    if payload == 'SUCCESS':
        assert response.data['teacher'] == teacher_create.id
        assert response.data['subject'] == subject_create.id
        assert response.data['grade'] == grade_create.id

    assert response.status_code == status_code
