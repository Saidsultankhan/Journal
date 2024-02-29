from rest_framework import serializers
from src.apps.jounal.models import Pupil


class ExcelGenerateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pupil
        fields = '__all__'