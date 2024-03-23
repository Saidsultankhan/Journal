
from rest_framework import permissions
from src.apps.jounal.models import SubjectTeacher


class TeacherOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True

        if SubjectTeacher.objects.filter(teacher__user=request.user, subject=obj).exists():
            return True

        return False
