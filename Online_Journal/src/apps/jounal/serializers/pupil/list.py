from src.apps.jounal.serializers.pupil.base import PupilBaseSerializer
from src.apps.jounal.models import Pupil, DairyOfClass
from rest_framework import serializers
from django.db.models import Avg


class PupilListSerializer(PupilBaseSerializer):
    grade = serializers.SerializerMethodField()

    class Meta:
        model = Pupil
        fields = ('id', 'name_en', 'grade', 'average_mark')

    def get_average_mark(self, obj):
        mark = DairyOfClass.objects.filter(pupil=obj).values_list('mark', flat=True)
        return obj.dairy_pupil.aggregate(average_mark=Avg('mark'))['average_mark'] if mark else 0

    def get_grade(self, obj):
        if obj.grade:
            return str(obj.grade)
        return f'Has not been added yet'
