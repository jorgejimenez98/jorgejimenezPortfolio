from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from experience.urls import router as experience_router
from social_media.urls import router as social_media_router
from projects.urls import router as projects_router
from main_settings.views import getSiteConfigurations, sendEmail
from .views import Main_TechViewSet, TechnologyViewSet

class DefaulRouter(routers.DefaultRouter):
    def extend(self, extra_router):
        self.registry.extend(extra_router.registry)

routerAux = DefaulRouter()
routerAux.extend(experience_router)
routerAux.extend(social_media_router)
routerAux.extend(projects_router)

router = routers.DefaultRouter()
router.register('technologies', TechnologyViewSet)
router.register('mainTech', Main_TechViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(routerAux.urls)),
    path('getSiteConfigurations/', getSiteConfigurations),
    path('sendEmail/', sendEmail),
]
