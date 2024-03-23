
from rest_framework import serializers
from src.apps.jounal.models import DairyOfClass


class DairyDetailSerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    pupil = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()

    class Meta:
        model = DairyOfClass
        fields = ('mark', 'subject_name', 'quarter', 'teacher', 'pupil', 'grade')

    def get_subject_name(self, obj):
        return {
            'id': obj.subject.id,
            'subject': obj.subject.name_uz
        }

    def get_teacher(self, obj):
        return {
            'id': obj.subject.subject_teacher_subject.first().teacher.id,
            'teacher': str(obj.subject.subject_teacher_subject.first().teacher)
        }

    def get_pupil(self, obj):
        return {
            'id': obj.pupil.id,
            'pupil': str(obj.pupil)
        }

    def get_grade(self, obj):
        return {
            'id': obj.grade.id,
            'class': str(obj.grade)
        }
