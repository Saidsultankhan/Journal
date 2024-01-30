from django.urls import path
from src.api import (
    PupilsViewSet,
    GradeViewSet,
    SubjectViewSet,
    TeacherViewSet,
    UserViewSet,
    DairyViewSet,
    SubjectTeacherViewSet,
    ParentsViewSet,
)

urlpatterns = [
    path('parent_create/', ParentsViewSet.as_view({'post': 'create'}), name="parent-create"),
    path('parent_update/<int:pk>/', ParentsViewSet.as_view({'patch': 'update'})),
    path('parent_delete/<int:pk>/', ParentsViewSet.as_view({'delete': 'destroy'})),
    path('parent_detail/<int:pk>/', ParentsViewSet.as_view({'get': 'retrieve'})),
    path('parents/', ParentsViewSet.as_view({'get': 'list'})),

    path('pupils/', PupilsViewSet.as_view({'get': 'list'})),
    path('pupil/<int:pk>/', PupilsViewSet.as_view({'get': 'retrieve'})),
    path('pupil_update/<int:pk>/', PupilsViewSet.as_view({'patch': 'update'})),
    path('pupil_delete/<int:pk>/', PupilsViewSet.as_view({'delete': 'destroy'})),
    path('pupil_create/', PupilsViewSet.as_view({'post': 'create'})),

    path('classes/', GradeViewSet.as_view({'get': 'list'})),
    path('class_create/', GradeViewSet.as_view({'post': 'create'})),
    path('class_update/<int:pk>/', GradeViewSet.as_view({'patch': 'update'})),
    path('class/<int:pk>/', GradeViewSet.as_view({'get': 'retrieve'})),

    path('subjects/', SubjectViewSet.as_view({'get': 'list'})),
    path('subject/<int:pk>/', SubjectViewSet.as_view({'get': 'retrieve'})),
    path('subject_create/', SubjectViewSet.as_view({'post': 'create'})),
    path('subject_update/<int:pk>/', SubjectViewSet.as_view({'patch': 'update'})),
    path('subject_delete/<int:pk>/', SubjectViewSet.as_view({'delete': 'destroy'})),

    path('subject_teachers/', SubjectTeacherViewSet.as_view({'get': 'list'})),
    path('subject_teacher/<int:pk>/', SubjectTeacherViewSet.as_view({'get': 'retrieve'})),
    path('subject_teacher/create/', SubjectTeacherViewSet.as_view({'post': 'create'})),
    path('subject_teacher/update/<int:pk>/', SubjectTeacherViewSet.as_view({'patch': 'update'})),
    path('subject_teacher/delete/<int:pk>/', SubjectTeacherViewSet.as_view({'delete': 'destroy'})),

    path('dairies/', DairyViewSet.as_view({'get': 'list'})),
    path('dairy/<int:pk>/', DairyViewSet.as_view({'get': 'retrieve'})),
    path('dairy_create/', DairyViewSet.as_view({'post': 'create'})),
    path('dairy_update/<int:pk>/', DairyViewSet.as_view({'patch': 'update'})),
    path('dairy_delete/<int:pk>/', DairyViewSet.as_view({'delete': 'destroy'})),

    path('teachers/', TeacherViewSet.as_view({'get': 'list'})),
    path('teacher/<int:pk>/', TeacherViewSet.as_view({'get': 'retrieve'})),
    path('teacher_create/', TeacherViewSet.as_view({'post': 'create'})),
    path('teacher_update/<int:pk>/', TeacherViewSet.as_view({'patch': 'update'})),
    path('teacher_delete/<int:pk>/', TeacherViewSet.as_view({'delete': 'destroy'})),

    path('unused_users_list/', UserViewSet.as_view({'get': 'list'})),
]

