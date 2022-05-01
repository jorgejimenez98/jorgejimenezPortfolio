from rest_framework import serializers
from technologie.serializers import TechnologieSerializer
from .models import Project, ProjectItem

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
