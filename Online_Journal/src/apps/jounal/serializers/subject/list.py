from rest_framework import serializers
from src.apps.jounal.models import Subject


class SubjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'name_uz')
