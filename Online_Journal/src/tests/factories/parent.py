import factory
from faker import Faker
from src.apps.jounal.models import Parent
from .user import UserFactory

fake = Faker()


class ParentFactory(factory.django.DjangoModelFactory):
    class Meta:
       model = Parent

    user = factory.SubFactory(UserFactory)
    name_uz = fake.user_name()
    name_ru = fake.user_name()
    name_en = fake.user_name()
