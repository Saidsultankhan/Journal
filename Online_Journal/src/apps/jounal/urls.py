from django.urls import path, include
from rest_framework.routers import DefaultRouter
from src.api import (
    PupilsViewSet,
    GradeViewSet,
    SubjectViewSet,
    TeacherViewSet,
    UserViewSet,
    DairyViewSet,
    SubjectTeacherViewSet,
    ParentsViewSet,
    ExcelGenerateViewSet,
    PDFGeneratorView,
    WordToPDFView,
)

router = DefaultRouter()

router.register(r'parents', ParentsViewSet)
router.register(r'pupils', PupilsViewSet)
router.register(r'classes', GradeViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'subject_teachers', SubjectTeacherViewSet)
router.register(r'dairies', DairyViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'unused_users_list', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('excel/', ExcelGenerateViewSet.as_view(), name='download_excel'),
    path('pdf/', PDFGeneratorView.as_view(), name='download_pdf'),
    path('word-to-pdf/', WordToPDFView.as_view(), name='word_to_pdf'),
]
