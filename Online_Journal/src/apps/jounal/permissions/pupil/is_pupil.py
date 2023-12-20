from rest_framework import permissions


class IsPupilOrAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

