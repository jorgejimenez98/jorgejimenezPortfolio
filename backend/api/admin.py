from django.contrib import admin
from solo.admin import SingletonModelAdmin
from . import models as m


admin.site.register(m.SiteConfiguration, SingletonModelAdmin)
admin.site.register(m.SocialMedia)
admin.site.register(m.Main_Tech)
admin.site.register(m.Technologie)
admin.site.register(m.Curriculum)
admin.site.register(m.ProjectItem)
admin.site.register(m.Project)
