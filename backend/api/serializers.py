from rest_framework import serializers
from .models import SiteConfiguration, SocialMedia


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
