import factory
from faker import Faker
from src.apps.jounal.models import Subject

fake = Faker()


class SubjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subject

    name_uz = fake.user_name()
    name_ru = fake.user_name()
    name_en = fake.user_name()
