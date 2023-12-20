from rest_framework import serializers
from src.apps.jounal.models import Pupil


class PupilDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = '__all__'

    def delete(self, instance):
        instance.delete()
