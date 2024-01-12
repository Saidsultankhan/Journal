from rest_framework import serializers
from src.apps.jounal.models import SubjectTeacher


class SubjectTeacherDetailSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()
    grades = serializers.SerializerMethodField()

    class Meta:
        model = SubjectTeacher
        fields = ('id', 'teacher', 'subject', 'grades')

    def get_teacher(self, obj):
        return {
            'user_id': obj.teacher.user.id,
            'name': obj.teacher.user.username

        }

    def get_subject(self, obj):
        return {
            'id': obj.subject.id,
            'name': obj.subject.name_uz
        }

    def get_grades(self, obj):
        return {
            'id': obj.grade.id,
            'name': str(obj.grade),
        }