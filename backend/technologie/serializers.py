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

    class Meta:
        model = Technologie
        fields = ['id', 'name', 'image_logo', 'icon_class', 'has_logo']


class TechnologieItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnologieItem
        fields = '__all__'
