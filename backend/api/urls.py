from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from main_settings.views import getSiteConfigurations, sendEmail
from experience.urls import router as experience_router
from social_media.urls import router as social_media_router
from projects.urls import router as projects_router
from technologie.urls import router as techs_router


class DefaulRouter(routers.DefaultRouter):
    def extend(self, extra_router):
        self.registry.extend(extra_router.registry)

router = DefaulRouter()
router.extend(experience_router)
router.extend(social_media_router)
router.extend(projects_router)
router.extend(techs_router)

urlpatterns = [
    path('', include(router.urls)),
    path('getSiteConfigurations/', getSiteConfigurations),
    path('sendEmail/', sendEmail),
]
