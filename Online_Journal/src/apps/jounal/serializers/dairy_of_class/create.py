from rest_framework import serializers
from src.apps.jounal.models import DairyOfClass, SubjectTeacher
from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import AuthenticationFailed


class DairyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DairyOfClass
        fields = ('mark', 'quarter', 'pupil', 'subject', 'grade')

    def create(self, validated_data):
        message = {
            'message': "У вас нет прав для добавления оценок в этот класс или по данному предмету."
        }
        request_user = self.context["request"].user

        # if not request_user.is_authenticated:
        #     raise AuthenticationFailed({"message": "Unauthorized"})

        teacher = self.context['request'].user.teacher_user.first()

        if teacher:
            subject = validated_data.get('subject')
            grade = validated_data.get('pupil').grade.id
            if SubjectTeacher.objects.filter(teacher=teacher, subject=subject, grade=grade).exists():
                return DairyOfClass.objects.create(**validated_data)
        else:
            raise PermissionDenied(message)

