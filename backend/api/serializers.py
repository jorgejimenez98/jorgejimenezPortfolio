from rest_framework import serializers
from .models import SiteConfiguration, SocialMedia, Main_Tech, Technologie, Curriculum, ProjectItem, \
    Project, Experience, TechnologieItem, KeyExperience
from datetime import date

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
    image_logo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Technologie
        fields = ['id', 'name', 'image_logo']

    def get_image_logo(self, obj):
        request = self.context.get('request')
        photo_url = request.build_absolute_uri(obj.image_logo.url)
        return photo_url


""" Curriculum Serializer """


class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = '__all__'


""" Projects Serializers """


class ProjectItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProjectItem
        fields = ['id', 'title', 'description', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        photo_url = request.build_absolute_uri(obj.image.url)
        return photo_url


class ProjectMiniSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'technologies']

    def get_technologies(self, obj):
        techs = obj.technologies.all()
        request = self.context.get('request')
        serializer = TechnologieSerializer(
            techs, many=True, context={"request": request})
        return serializer.data


class ProjectSerializer(ProjectMiniSerializer):
    projectItems = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description',
                  'repositoryUrl', 'technologies', 'projectItems']

    def get_projectItems(self, obj):
        projectItems = obj.projectItems.all()
        request = self.context.get('request')
        serializer = ProjectItemSerializer(
            projectItems, many=True, context={'request': request})
        return serializer.data


""" Experience Serializer """

# Experience, TechnologieItem, KeyExperience


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