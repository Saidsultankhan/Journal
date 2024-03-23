from rest_framework import serializers
from src.apps.jounal.models import (
    DairyOfClass,
    Grade,
    Teacher,
    Pupil,
    Subject
)


class DairyUpdateSerializer(serializers.ModelSerializer):
    mark = serializers.IntegerField(required=False)
    pupil = serializers.PrimaryKeyRelatedField(queryset=Pupil.objects.all(), required=False)
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), required=False)
    quarter = serializers.IntegerField(required=False)
    grade = serializers.PrimaryKeyRelatedField(queryset=Grade.objects.all(), required=False)

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
