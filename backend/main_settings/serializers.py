from rest_framework import serializers
from .models import SiteConfiguration, TranslationText

class TranslationTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationText
        fields = ['language', 'text']


class SiteConfigurationSerializer(serializers.ModelSerializer):
    main_presentations = serializers.SerializerMethodField(read_only=True)
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
            'main_presentations',
        ]

    def get_profilePicture(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(obj.profilePicture.url)
    
    def get_main_presentations(self, obj):
        main_presentations = obj.main_presentations.all()
        print(main_presentations)
        return TranslationTextSerializer(main_presentations, many=True).data