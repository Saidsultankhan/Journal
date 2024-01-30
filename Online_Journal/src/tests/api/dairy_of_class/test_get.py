import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.parametrize(
    "client, status_code, payload",
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('teacher_client', 200, "SUCCESS"),
        ('teacher_client', 404, "NOT_FOUND"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_teacher_get_dairy(
        request,
        client,
        status_code,
        payload,
        get_data,
        teacher_create
):
    auth_client_data = request.getfixturevalue(client)
    auth_client, user = auth_client_data["client"], auth_client_data["user"]

    if client in ['un_authorized_client', 'parent_client']:
        user = teacher_create
    data = get_data(user)

    response = auth_client.get(f'/api/v1/dairy/{data[payload]["dairy_id"]}/')

    assert response.status_code == status_code


@pytest.fixture
def get_data(
        subject_factory,
        subject_teacher_factory,
        grade_factory,
        pupil_factory,
        dairy_of_class_factory,
        teacher_create_for_dairy,
):
    subject = subject_factory.create()
    grade = grade_factory.create()
    pupil = pupil_factory.create(grade=grade)

    def create_date(user):
        subject_teacher_factory.create(teacher_id=user.id, subject=subject, grade=grade)
        dairy = dairy_of_class_factory.create(grade=grade, subject=subject, pupil=pupil)

        data = {
            'FORBIDDEN': {
                'dairy_id': dairy.id
            },
            'NOT_FOUND': {
                'dairy_id': dairy.id + 1
            },
            'SUCCESS': {
                'dairy_id': dairy.id
            },
            'UNAUTHORIZED': {
                'dairy_id': dairy.id
            },
        }

        return data

    return create_date
