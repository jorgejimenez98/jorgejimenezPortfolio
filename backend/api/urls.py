from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from experience.urls import router as experience_router
from main_settings.views import getSiteConfigurations, sendEmail
from .views import SocialMediaViewSet, Main_TechViewSet, TechnologyViewSet, \
    CurriculumViewSet, ProjectViewSet

class DefaulRouter(routers.DefaultRouter):
    def extend(self, extra_router):
        self.registry.extend(extra_router.registry)

routerAux = DefaulRouter()
routerAux.extend(experience_router)

router = routers.DefaultRouter()
router.register('socialMedias', SocialMediaViewSet)
router.register('technologies', TechnologyViewSet)
router.register('mainTech', Main_TechViewSet)
router.register('curriculumns', CurriculumViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(routerAux.urls)),
    path('getSiteConfigurations/', getSiteConfigurations),
    path('sendEmail/', sendEmail),
]
