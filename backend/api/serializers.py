from rest_framework import serializers
from .models import Main_Tech, Technologie


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
