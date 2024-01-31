import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    "client, status_code, payload",
    [
        ('parent_client', 403, "FORBIDDEN"),
        ('teacher_client', 200, "SUCCESS"),
        ('un_authorized_client', 401, "UNAUTHORIZED"),
    ]
)
@pytest.mark.django_db
def test_teacher_list_dairy(
        request,
        client,
        status_code,
        payload,
        teacher_create,
        subject_factory,
        subject_teacher_factory,
        grade_factory,
        pupil_factory,
        dairy_of_class_factory,
        teacher_create_for_dairy,
):
    if client in ['un_authorized_client', 'parent_client']:
        user = teacher_create
    else:
        user = request.getfixturevalue(client)["user"]

    auth_client = request.getfixturevalue(client)["client"]

    subject = subject_factory.create()
    grade = grade_factory.create()
    pupil = pupil_factory.create(grade=grade)
    subject_teacher_factory.create(teacher_id=user.id, subject=subject, grade=grade)
    dairy = dairy_of_class_factory.create_batch(size=3, grade=grade, subject=subject, pupil=pupil)
    url = reverse('dairyofclass-list')

    response = auth_client.get(url)

    if payload == 'SUCCESS':
        assert len(response.data) == len(dairy)

    assert response.status_code == status_code
