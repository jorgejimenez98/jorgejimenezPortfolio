from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from main_settings.views import getSiteConfigurations, sendEmail
from .views import SocialMediaViewSet, Main_TechViewSet, TechnologyViewSet, \
    CurriculumViewSet, ProjectViewSet, KeyExperienceViewSet, ExperienceViewSet, TechnologieItemViewSet

router = routers.DefaultRouter()
router.register('socialMedias', SocialMediaViewSet)
router.register('technologies', TechnologyViewSet)
router.register('mainTech', Main_TechViewSet)
router.register('curriculumns', CurriculumViewSet)
router.register('projects', ProjectViewSet)
router.register('techItems', TechnologieItemViewSet)
router.register('expertises', ExperienceViewSet)
router.register('keyExperiences', KeyExperienceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getSiteConfigurations/', getSiteConfigurations),
    path('sendEmail/', sendEmail),
]
