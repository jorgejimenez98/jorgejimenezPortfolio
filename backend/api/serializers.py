from rest_framework import serializers
from .models import SiteConfiguration, SocialMedia, Main_Tech, Technologie, Curriculum


""" Site Configuration Serializer """


class SiteConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteConfiguration
        fields = "__all__"


""" Social Media Serializer """


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


""" Tech Serializers """


class Main_TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_Tech
        fields = '__all__'


class TechnologieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technologie
        fields = '__all__'


""" Curriculum Serializer """


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'
