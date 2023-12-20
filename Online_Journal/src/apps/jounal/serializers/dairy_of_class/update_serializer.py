from rest_framework import serializers
from src.apps.jounal.models import DairyOfClass


class DairyUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = DairyOfClass
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.mark = validated_data.get('mark', instance.mark)
        instance.quarter = validated_data.get('quarter', instance.quarter)
        instance.pupil = validated_data.get('pupil', instance.pupil)
        instance.subject = validated_data.get('subject', instance.subject)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.save()
        return instance