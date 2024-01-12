from rest_framework import serializers
from django.db.models import Avg


class PupilBaseSerializer(serializers.ModelSerializer):
    average_mark = serializers.SerializerMethodField()

    def get_average_mark(self, obj):
        return obj.dairy_pupil.aggregate(average_mark=Avg('mark'))['average_mark']