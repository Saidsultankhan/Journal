import factory
from .teacher import TeacherFactory
from faker import Faker
from itertools import cycle
from src.apps.jounal.static_data import TYPE_CHOICES
from src.apps.jounal.models import Grade

fake = Faker()


class GradeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Grade

    number = factory.Iterator(cycle(range(1, 12)))
    type = fake.random_element(elements=[choice[0] for choice in TYPE_CHOICES])
    teacher = factory.SubFactory(TeacherFactory)
