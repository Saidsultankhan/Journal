from src.apps.jounal.serializers.pupil.pupil_base import PupilBaseSerializer
from src.apps.jounal.models import Pupil, DairyOfClass
from rest_framework import serializers
from django.db.models import Avg


class PupilListSerializer(PupilBaseSerializer):
    grade = serializers.CharField(source='grade.__str__')

    class Meta:
        model = Pupil
        fields = ('id', 'name_en', 'grade', 'average_mark')

    def get_average_mark(self, obj):
        mark = DairyOfClass.objects.filter(pupil=obj).values_list('mark', flat=True)
        return obj.dairy_pupil.aggregate(average_mark=Avg('mark'))['average_mark'] if mark else 0
