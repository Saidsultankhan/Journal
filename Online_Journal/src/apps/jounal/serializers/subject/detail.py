from rest_framework import serializers
from src.apps.jounal.models import Subject, SubjectTeacher


class SubjectDetailSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ('id', 'name_uz', 'name_ru', 'name_en', 'teachers')

    def get_teachers(self, obj):
        teachers = SubjectTeacher.objects.filter(subject=obj).select_related('teacher', 'grade')
        teacher_details = [
            {
                'teacher_name': teacher_object.teacher.user.username,
                'class_name': str(teacher_object.grade)
            }
            for teacher_object in teachers
        ]
        return teacher_details
