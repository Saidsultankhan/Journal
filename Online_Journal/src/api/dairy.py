from rest_framework import viewsets
from src.apps.jounal.models import DairyOfClass
from src.apps.jounal.serializers import (
    DairyOfClassSerializer,
    DairyDetailSerializer,
    DairyCreateSerializer,
    DairyUpdateSerializer,
    DairyDeleteSerializer,
)
from src.apps.jounal.permissions import DairyTeacher, DairyListTeacher
from rest_framework.permissions import IsAuthenticated


class DairyViewSet(viewsets.ModelViewSet):
    queryset = DairyOfClass.objects.all()
    # def get_queryset(self):
    #     user = self.request.user
    #
    #     if user.is_staff:
    #         return DairyOfClass.objects.all().order_by("grade")
    #
    #     else:
    #         teacher_user = user.teacher_user.first()
    #         mentor = teacher_user.class_teacher.first()

            # subjects = [subject.id for subject in teacher_user.subject_teacher_teacher.all().only("subject")]
            # print(subjecst, "!")
            # grades = [grade.id for grade in teacher_user.subject_teacher_teacher.all()]
            # print(grades, "2")
            # qs = list()

            # for grade_id in grades:
                # qs += list(DairyOfClass.objects.filter(grade_id=grade_id))
                # qs.append(DairyOfClass.objects.filter(grade_id=grade_id).first())
            # qs = DairyOfClass.objects.filter(
            #     grade__class_teacher_teacher__teacher=teacher_user,
            #     subject__subject__subject_teacher_subject=teacher_user.subject_teacher_teacher,
            # )

            # print(qs)

            # print(grade_ids)
            # qs = DairyOfClass.objects.filter(subject__subject_teacher_subject_id=teacher_user.id).order_by("subject", "grade")

            # grade_ids = [instance.grade.id for instance in teacher_user.subject_teacher_teacher.all()]

            # if mentor:
            #     qs += DairyOfClass.objects.filter(grade__teacher__user=user).order_by("subject")

            # return set(qs)
            # return qs

    def get_serializer_class(self):
        serializers = {
            'retrieve': DairyDetailSerializer,
            'create': DairyCreateSerializer,
            'list': DairyOfClassSerializer,
            'delete': DairyDeleteSerializer,
            'update': DairyUpdateSerializer
        }
        return serializers.get(self.action)

    def get_permissions(self):
        permission_classes = []
        if self.action in ['retrieve', 'create', 'update', 'destroy']:
            permission_classes = [IsAuthenticated, DairyTeacher]
        elif self.action in ["list"]:
            permission_classes = [IsAuthenticated, DairyListTeacher]

        return [permission_class() for permission_class in permission_classes]
