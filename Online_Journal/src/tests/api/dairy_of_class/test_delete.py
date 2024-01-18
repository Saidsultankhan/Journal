import pytest
from rest_framework.test import APIClient


api_client = APIClient()


@pytest.mark.django_db
def test_teacher_delete_dairy(
        teacher_client,
        subject_factory,
        subject_teacher_factory,
        grade_factory,
        pupil_factory,
        dairy_of_class_factory
):
    client = teacher_client.get("client")
    teacher = teacher_client["user"]
    subject = subject_factory.create()
    grade = grade_factory.create()
    pupil = pupil_factory.create(grade=grade)
    subject_teacher = subject_teacher_factory.create(teacher_id=teacher.id, subject=subject, grade=grade)
    dairy = dairy_of_class_factory.create(grade=grade, subject=subject, pupil=pupil)
    response = client.delete(f'/api/v1/dairy_delete/{dairy.id}/')

    assert response.status_code == 204
    