from rest_framework import permissions
from src.apps.jounal.models import Teacher, Pupil


class IsTeacherOrMentorOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        if Teacher.objects.filter(user=request.user).exists():
            return obj.teacher.user == request.user
        if Teacher.objects.filter(user=request.user).exists():
            return obj.subject_teacher_class.teacher.user == request.user
        if Pupil.objects.filter(user=request.user, grade=obj).exists():
            return True
