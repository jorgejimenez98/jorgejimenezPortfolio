from rest_framework import serializers
from .models import SiteConfiguration, TranslationText

class TranslationTextSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = TranslationText
        fields = ['language', 'text']
    
    def get_text(self, obj):
        if 'años' in obj.text or 'years' in obj.text:
            years = obj.site_config_presentations.get().years_of_experience
            return str(obj.text).replace('2', str(years).replace('.', ','))
        return obj.text


class SiteConfigurationSerializer(serializers.ModelSerializer):
    main_presentations = serializers.SerializerMethodField(read_only=True)
    title_presentations = serializers.SerializerMethodField(read_only=True)
    profilePicture = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SiteConfiguration
        fields = [
            'developer_name',
            'years_of_experience',
            'is_open_to_work',
            'phone_number',
            'repository_project_url',
            'developer_email',
            'profilePicture',
            'title_presentations',
            'main_presentations',
        ]

    def get_profilePicture(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(obj.profilePicture.url)
    
    def get_main_presentations(self, obj):
        main_presentations = obj.main_presentations.all()
        return TranslationTextSerializer(main_presentations, many=True).data

    def get_title_presentations(self, obj):
        title_presentations = obj.title_presentations.all()
        return TranslationTextSerializer(title_presentations, many=True).data