from rest_framework import serializers
from src.apps.jounal.models import Parent, Pupil
# from src.apps.jounal.serializers import PupilDetailSerializer


class ParentDetailSerializer(serializers.ModelSerializer):
    pupils = serializers.SerializerMethodField()

    class Meta:
        model = Parent
        fields = ('id', 'user', 'pupils')

    def get_pupils(self, obj):
        pupils = Pupil.objects.filter(parent=obj.id)
        return [{
            'id': pupil.id,
            'name_uz': pupil.name_uz,
            'name_ru': pupil.name_ru,
            'name_en': pupil.name_en,
            'grade': str(pupil.grade),
        }
            for pupil in pupils
        ]