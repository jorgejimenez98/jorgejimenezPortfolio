from rest_framework.routers import DefaultRouter
from .views import KeyExperienceViewSet, ExperienceViewSet

router = DefaultRouter()
router.register('expertises', ExperienceViewSet)
router.register('keyExperiences', KeyExperienceViewSet)