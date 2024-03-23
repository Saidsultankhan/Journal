from rest_framework import serializers
from src.apps.jounal.models import Grade


class GradeDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

    def delete(self, instance):
        instance.delete()
