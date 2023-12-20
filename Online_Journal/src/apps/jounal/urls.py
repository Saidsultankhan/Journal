from django.urls import path
from src.api import (
    PupilsViewSet,
    ClassViewSet,
    SubjectViewSet,
    TeacherViewSet,
    UserViewSet,
    DairyViewSet,
    SubjectTeacherViewSet
)

urlpatterns = [
    path('pupils/', PupilsViewSet.as_view({'get': 'list'})),
    path('pupil/<int:pk>/', PupilsViewSet.as_view({'get': 'retrieve'})),
    path('pupil_update/<int:pk>/', PupilsViewSet.as_view({'patch': 'update'})),
    path('pupil_delete/<int:pk>/', PupilsViewSet.as_view({'delete': 'destroy'})),
    path('pupil_create/', PupilsViewSet.as_view({'post': 'create'})),
    path('classes/', ClassViewSet.as_view({'get': 'list'})),
    path('class_create/', ClassViewSet.as_view({'post': 'create'})),
    path('class_update/<int:pk>', ClassViewSet.as_view({'patch': 'update'})),
    path('class/<int:pk>/', ClassViewSet.as_view({'get': 'retrieve'})),
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

