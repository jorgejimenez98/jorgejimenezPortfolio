from django.contrib import admin
from solo.admin import SingletonModelAdmin
from . import models as m

admin.site.register(m.SiteConfiguration, SingletonModelAdmin)
admin.site.register(m.TranslationText)