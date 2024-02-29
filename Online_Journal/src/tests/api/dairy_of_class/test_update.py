import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    "client, status_code, payload",
    [
        ('teacher_client', 200, "SUCCESS"),
        ('teacher_client', 400, "BAD_REQUEST"),
        ('parent_client', 403, "FORBIDDEN"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_dairy_update(
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

    datas = get_data(user)
    url = reverse('dairyofclass-detail', kwargs={'pk': datas["dairy"].id})
    response = auth_client.patch(url, datas['data'][payload])
    
    assert response.status_code == status_code


@pytest.fixture
def get_data(
        subject_factory,
        subject_teacher_factory,
        grade_factory,
        pupil_factory,
        dairy_of_class_factory,
):
    subject = subject_factory.create()
    grade = grade_factory.create()
    pupil = pupil_factory.create(grade=grade)

    def create_date(user):
        subject_teacher_factory.create(teacher_id=user.id, subject=subject, grade=grade)
        dairy = dairy_of_class_factory.create(grade=grade, subject=subject, pupil=pupil)
        statuses = ['FORBIDDEN', 'BAD_REQUEST', 'SUCCESS', 'UNAUTHORIZED']

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

        return {'data': datas, 'dairy': dairy}

    return create_date
