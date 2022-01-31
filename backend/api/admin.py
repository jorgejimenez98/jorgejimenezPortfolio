from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteConfiguration, SocialMedia, Main_Tech, Technologie, Curriculum


admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(SocialMedia)
admin.site.register(Main_Tech)
admin.site.register(Technologie)
admin.site.register(Curriculum)