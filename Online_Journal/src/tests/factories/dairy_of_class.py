import factory
from faker import Faker
from .pupil import PupilFactory
from .subject import SubjectFactory
from .grade import GradeFactory
from src.apps.jounal.models import DairyOfClass

fake = Faker()


class DairyOfClassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DairyOfClass

    mark = fake.random_element(elements=range(1, 6))
    pupil = factory.SubFactory(PupilFactory)
    subject = factory.SubFactory(SubjectFactory)
    quarter = fake.random_element(elements=range(1, 5))
    grade = factory.SubFactory(GradeFactory)
