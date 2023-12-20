from rest_framework import viewsets
from django.contrib.auth.models import User
from src.apps.jounal.serializers import UnusedUserListSerializer


class UserViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        teacher = self.request.query_params.get("teacher", None)
        pupil = self.request.query_params.get("pupil", None)
        parent = self.request.query_params.get("parent", None)
        queryset = User.objects.filter(
            teacher_user__isnull=False if teacher == "True" else True,
            parent_user__isnull=False if parent == "True" else True,
            pupil_user__isnull=False if pupil == "True" else True
        )

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return UnusedUserListSerializer
