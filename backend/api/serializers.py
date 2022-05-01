from rest_framework import serializers
from .models import SocialMedia, Main_Tech, Technologie, Curriculum, ProjectItem, \
    Project


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
            projectItems, many=True, context={'request': request}
        )
        return serializer.data
