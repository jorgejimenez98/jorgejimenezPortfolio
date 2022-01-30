from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration, SocialMedia


admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(SocialMedia)