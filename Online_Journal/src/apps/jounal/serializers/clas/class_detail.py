from rest_framework import serializers
from src.apps.jounal.models import Class, SubjectTeacher


class ClassDetailSerializer(serializers.ModelSerializer):
    mentor = serializers.SerializerMethodField(source='teacher')
    name = serializers.CharField(source='__str__')
    pupils_number = serializers.SerializerMethodField()
    class_pupil = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = ('mentor', 'name', 'pupils_number', 'class_pupil', 'subjects')

    def get_parent_name_uz(self, parent_instance):
        return parent_instance.name_uz if parent_instance else None

    def get_class_pupil(self, obj):
        pupils_list = []
        for pupil in obj.class_pupil.all():
            parent = pupil.parent
            parent_name_uz = parent.user.username if parent else None
            pupils_list.append({
                'id': pupil.id,
                'name_uz': pupil.name_uz,
                'name_ru': pupil.name_ru,
                'name_en': pupil.name_en,
                'parent': parent_name_uz,
            })
        sorted_pupils = sorted(pupils_list, key=lambda x: x['name_uz'])

        numbered_pupils = [{
            **pupil_info,
            'number_in_dairy': idx + 1,
        } for idx, pupil_info in enumerate(sorted_pupils)]

        return numbered_pupils

    def get_pupils_number(self, obj):
        return obj.class_pupil.count()

    def get_mentor(self, obj):
        data = {
            "id": obj.teacher.id,
            "username": obj.teacher.user.username
        }
        return data

    def get_subjects(self, obj):
        subjects = SubjectTeacher.objects.filter(grade=obj).select_related('subject', 'teacher')
        subject = [
            {
                'id': subject.subject.id,
                'name_uz': subject.subject.name_uz,
                'teacher': subject.teacher.user.username
            }
            for subject in subjects
        ]
        return subject
