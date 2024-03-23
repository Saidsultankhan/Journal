from rest_framework import serializers
from src.apps.jounal.models import Subject


class SubjectDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'

    def delete(self, instance):
        instance.delete()