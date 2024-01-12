from rest_framework import serializers
from src.apps.jounal.models import Teacher, SubjectTeacher


class TeacherDetailSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    mentor_of = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'grade', 'subjects', 'mentor_of')

    def get_name(self, obj):
        return obj.user.username

    def get_grade(self, obj):
        return [
            {
                'id': grade.id,
                'class': str(grade)}
            for grade in obj.class_teacher.all()
        ]

    def get_mentor_of(self, obj):
        return [
            [
                {
                    'id': j.user.id,
                    'name': j.user.username}
                for j in i.class_pupil.all()]
            for i in obj.class_teacher.all() if i.class_pupil.exists()]

    def get_subjects(self, obj):
        return [
            {'id': subject.id, 'subject': str(subject.subject)}
            for subject in SubjectTeacher.objects.filter(teacher=obj).all()
        ]
