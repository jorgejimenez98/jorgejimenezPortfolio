from rest_framework import serializers
from .models import *
from main_settings.serializers import TranslationTextSerializer


class KeyExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyExperience
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    key_experiences = serializers.StringRelatedField(many=True)
    techs = serializers.StringRelatedField(many=True)
    time_working = serializers.SerializerMethodField(read_only=True)
    job_rols = serializers.SerializerMethodField(read_only=True)
    company_names = serializers.SerializerMethodField(read_only=True)
    descriptions = serializers.SerializerMethodField(read_only=True)
    locations = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Experience
        fields = [
            'id',
            'date_start',
            'date_end',
            'is_currently_working',
            'time_working',
            'key_experiences',
            'techs',
            'company_logo',
            'job_rols',
            'company_names',
            'descriptions',
            'locations'
        ]

    def get_time_working(self, obj):
        return [
            {
                'language': 'es',
                'text': obj.get_time_working('es')
            },
            {
                'language': 'en',
                'text': obj.get_time_working('en')
            },
        ]

    def get_job_rols(self, obj):
        return TranslationTextSerializer(obj.job_rols.all(), many=True).data

    def get_company_names(self, obj):
        return TranslationTextSerializer(obj.conmpany_names.all(), many=True).data

    def get_descriptions(self, obj):
        return TranslationTextSerializer(obj.descriptions.all(), many=True).data

    def get_locations(self, obj):
        return TranslationTextSerializer(obj.locations.all(), many=True).data
