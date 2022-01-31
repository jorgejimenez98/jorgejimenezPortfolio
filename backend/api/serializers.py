from rest_framework import serializers
from .models import SiteConfiguration, SocialMedia, Main_Tech, Technologie, Curriculum, ProjectItem, Project


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


""" Projects Serializers """


class ProjectItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItem
        fields = '__all__'


class ProjectMiniSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'technologies']

    def get_technologies(self, obj):
        techs = Technologie.objects.filter(project__id=obj.pk)
        serializer = TechnologieSerializer(techs)
        return serializer.data


class ProjectSerializer(ProjectMiniSerializer):
    projectItems = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'technologies', 'projectItems']

    def get_projectItems(self, obj):
        projectItems = obj.projectItems.all()
        serializer = ProjectItemSerializer(projectItems)
        return serializer.data
