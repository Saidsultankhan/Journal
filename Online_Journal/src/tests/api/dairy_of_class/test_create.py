import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.parametrize(
    "client, status_code, payload",
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('teacher_client', 201, "SUCCESS"),
        ('teacher_client', 400, "BAD_REQUEST"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_dairy_create(
        request,
        client,
        status_code,
        payload,
        get_data,
        teacher_create,
):
    auth_client_data = request.getfixturevalue(client)
    auth_client, user = auth_client_data["client"], auth_client_data["user"]

    if client in ['un_authorized_client', 'parent_client']:
        user = teacher_create

    data = get_data(user)

    response = auth_client.post(f'/api/v1/dairy_create/', data[payload])

    if status_code == 201:
        assert response.data['pupil'] == data['SUCCESS']['pupil']
        assert response.data['mark'] == data['SUCCESS']['mark']
        assert response.data['subject'] == data['SUCCESS']['subject']
        assert response.data['quarter'] == data['SUCCESS']['quarter']
        assert response.data['grade'] == data['SUCCESS']['grade']

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
        dairy_of_class_factory.create(grade=grade, subject=subject, pupil=pupil)
        statuses = ['FORBIDDEN', 'BAD_REQUEST', 'SUCCESS', 'UNAUTHORIZED']

        # datas = {status: {
        #     'mark': 1,
        #     'pupil': pupil.id,
        #     'subject': subject.id,
        #     'grade': grade.id,
        #     'quarter': 2
        # }
        #     if status != 'BAD_REQUEST'
        #     else {
        #     'mark': 1,
        #     'pupil': pupil.id,
        #     'subject': 1000,
        #     'grade': grade.id,
        #     'quarter': 2
        # }
        #     for status in statuses}

        datas = {}

        for status in statuses:
            datas[status] = {
                    'mark': 1,
                    'pupil': pupil.id,
                    'subject': subject.id,
                    'grade': grade.id,
                    'quarter': 2,
                }

            if status == 'BAD_REQUEST':
                datas[status]['subject'] = 1000

        return datas

    return create_date
