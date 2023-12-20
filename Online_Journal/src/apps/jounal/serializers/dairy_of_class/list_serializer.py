from rest_framework import serializers
from src.apps.jounal.models import DairyOfClass


class DairyOfClassSerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()
    pupil = serializers.SerializerMethodField()

    class Meta:
        model = DairyOfClass
        fields = ('mark', 'subject_name', 'quarter', 'teacher', 'pupil')

    def get_subject_name(self, obj):
        return obj.subject.name_uz

    def get_teacher(self, obj):
        return str(obj.subject.subject_teacher_subject.first().teacher)

    def get_pupil(self, obj):
        return str(obj.pupil)
