import factory
from django.contrib.auth.models import User
from faker import Faker
from itertools import cycle
from src.apps.jounal.static_data import (
    MARK_CHOICES,
    QUARTER_CHOICES,
    TYPE_CHOICES
)
from src.apps.jounal.models import (
    Parent,
    Pupil,
    Teacher,
    Grade,
)

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user_{n}')
    password = '23456789'
    email = fake.email()
    is_staff = False


class ParentFactory(factory.django.DjangoModelFactory):
    class Meta:
       model = Parent

    user = factory.SubFactory(UserFactory)
    name_uz = fake.user_name()
    name_ru = fake.user_name()
    name_en = fake.user_name()


class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Teacher

    user = factory.SubFactory(UserFactory)


class GradeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Grade

    number = factory.Iterator(cycle(range(1, 12)))
    type = fake.random_element(elements=[choice[0] for choice in TYPE_CHOICES])
    teacher = factory.SubFactory(TeacherFactory)


class PupilFactory(factory.django.DjangoModelFactory):
    class Meta:
       model = Pupil

    name_uz = fake.user_name()
    name_ru = fake.user_name()
    name_en = fake.user_name()
    user = factory.SubFactory(UserFactory)
    grade = factory.SubFactory(GradeFactory)
    parent = factory.SubFactory(ParentFactory)
