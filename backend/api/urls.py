from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import getSiteConfigurations, SocialMediaViewSet, Main_TechViewSet, TechnologyViewSet, CurriculumViewSet

router = routers.DefaultRouter()
router.register('socialMedias', SocialMediaViewSet)
router.register('technologies', TechnologyViewSet)
router.register('mainTech', Main_TechViewSet)
router.register('curriculumns', CurriculumViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getSiteConfigurations/', getSiteConfigurations),
]
