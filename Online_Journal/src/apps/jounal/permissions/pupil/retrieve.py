from rest_framework import permissions
from src.apps.jounal.models import Pupil, Parent, Teacher


class IsTeacherOrPupilOrParentOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        if Teacher.objects.filter(user=request.user).exists():
            return obj.grade.teacher.user == request.user
        if Parent.objects.filter(user=request.user).exists():
            return obj.parent.user == request.user
        if Pupil.objects.filter(user=request.user).exists():
            return obj.user == request.user
