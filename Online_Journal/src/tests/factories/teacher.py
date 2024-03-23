import factory
from faker import Faker
from .user import UserFactory
from src.apps.jounal.models import Teacher

fake = Faker()


class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserFactory)
