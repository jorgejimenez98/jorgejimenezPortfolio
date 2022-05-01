from rest_framework import serializers
from .models import *


class KeyExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyExperience
        fields = '__all__'


class TechnologieItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologieItem
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    key_experiences = serializers.SerializerMethodField(read_only=True)
    techs = serializers.SerializerMethodField(read_only=True)
    time_working = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Experience
        fields = [
            'id',
            'date_start',
            'date_end',
            'is_currently_working',
            'company_logo',
            'job_rol',
            'conmpany_name',
            'description',
            'time_working',
            'key_experiences',
            'techs',
        ]

    def get_key_experiences(self, obj):
        data = obj.key_experiences.all()
        serializer = KeyExperienceSerializer(data, many=True)
        return serializer.data

    def get_techs(self, obj):
        data = obj.techs.all()
        serializer = TechnologieItemSerializer(data, many=True)
        return serializer.data

    def get_time_working(self, obj):
        if obj.is_currently_working:
            return date.today() - obj.date_start
        return obj.date_end - obj.date_start