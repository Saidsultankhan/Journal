from rest_framework import serializers
from src.apps.jounal.models import DairyOfClass


class DairyDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = DairyOfClass
        fields = '__all__'

    def delete(self, instance):
        instance.delete()