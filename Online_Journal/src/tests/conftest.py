from pytest_factoryboy import register
from .fixtures import *
from .factories.user import UserFactory
from .factories.parent import ParentFactory
from .factories.teacher import TeacherFactory
from .factories.grade import GradeFactory
from .factories.pupil import PupilFactory
from .factories.subject import SubjectFactory
from .factories.subject_teacher import SubjectTeacherFactory
from .factories.dairy_of_class import DairyOfClassFactory

register(UserFactory)
register(ParentFactory)
register(TeacherFactory)
register(GradeFactory)
register(PupilFactory)
register(SubjectFactory)
register(SubjectTeacherFactory)
register(DairyOfClassFactory)
