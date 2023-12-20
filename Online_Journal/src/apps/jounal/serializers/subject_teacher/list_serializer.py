from rest_framework import serializers
from src.apps.jounal.models import SubjectTeacher


class SubjectTeacherListSerializer(serializers.ModelSerializer):
    subject = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = SubjectTeacher
        fields = ('id', 'subject', 'teacher')

    def get_subject(self, obj):
        return obj.subject.name_uz

    def get_teacher(self, obj):
        return str(obj.subject.subject_teacher_subject.first().teacher)
