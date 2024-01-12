from src.apps.jounal.serializers.pupil.base import PupilBaseSerializer
from rest_framework import serializers
from src.apps.jounal.models import (
    Pupil,
    DairyOfClass,
    SubjectTeacher
)
from django.db.models import Avg


class PupilDetailSerializer(PupilBaseSerializer):
    pupils_dairy = serializers.SerializerMethodField(source='dairy_pupils')
    grade = serializers.SerializerMethodField()
    parent = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = Pupil
        fields = ('id', 'name_en', 'name_ru', 'name_uz', 'parent', 'grade', 'average_mark', 'pupils_dairy', 'teachers')

    def get_parent(self, obj):
        return obj.parent.user.username

    def get_pupils_dairy(self, obj):
        unique_subjects = DairyOfClass.objects.filter(
            pupil__id=obj.id
        ).values_list('subject__name_uz', flat=True).distinct()

        subjects_data = []
        for subject in unique_subjects:
            average_mark = DairyOfClass.objects.filter(
                subject__name_uz=subject,
                pupil__id=obj.id
            ).aggregate(average_mark=Avg('mark'))['average_mark']

            subject_marks = self.get_subject_marks(obj, subject)
            subjects_data.append({
                'subject_name': subject,
                'average_subject_mark': average_mark,
                f'all_marks_in_{subject}': subject_marks
            })
        return subjects_data

    def get_teachers(self, obj):
        subject_teachers = SubjectTeacher.objects.filter(grade=obj.grade).select_related('subject', 'teacher')
        class_subject_teachers = [
            {
                'subject': subject.subject.name_uz,
                'teacher': subject.teacher.user.username,
            }
            for subject in subject_teachers
        ]
        return class_subject_teachers

    def get_grade(self, obj):
        return {
            'class_name': str(obj.grade),
            'mentor': str(obj.grade.teacher),
        }
