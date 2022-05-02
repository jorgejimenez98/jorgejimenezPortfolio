from rest_framework import serializers
from .models import Main_Tech, Technologie, TechnologieItem
from main_settings.serializers import TranslationTextSerializer


class Main_TechSerializer(serializers.ModelSerializer):
    texts = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Main_Tech
        fields = ['id', 'proccessPorcent', 'texts']
    
    def get_texts(self, obj):
        return TranslationTextSerializer(obj.texts.all(), many=True).data


class TechnologieSerializer(serializers.ModelSerializer):
    image_logo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Technologie
        fields = ['id', 'name', 'image_logo']

    def get_image_logo(self, obj):
        request = self.context.get('request')
        photo_url = request.build_absolute_uri(obj.image_logo.url)
        return photo_url

class TechnologieItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologieItem
        fields = '__all__'