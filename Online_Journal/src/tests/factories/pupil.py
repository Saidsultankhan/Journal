import factory
from faker import Faker
from .user import UserFactory
from .grade import GradeFactory
from .parent import ParentFactory
from src.apps.jounal.models import Pupil

fake = Faker()


class PupilFactory(factory.django.DjangoModelFactory):
    class Meta:
       model = Pupil

    name_uz = fake.user_name()
    name_ru = fake.user_name()
    name_en = fake.user_name()
    user = factory.SubFactory(UserFactory)
    grade = factory.SubFactory(GradeFactory)
    parent = factory.SubFactory(ParentFactory)
