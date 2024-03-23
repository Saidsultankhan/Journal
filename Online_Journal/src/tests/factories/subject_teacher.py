import factory
from faker import Faker
from .teacher import TeacherFactory
from .subject import SubjectFactory
from .grade import GradeFactory
from src.apps.jounal.models import SubjectTeacher

fake = Faker()


class SubjectTeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SubjectTeacher

    teacher = factory.SubFactory(TeacherFactory)
    subject = factory.SubFactory(SubjectFactory)
    grade = factory.SubFactory(GradeFactory)
