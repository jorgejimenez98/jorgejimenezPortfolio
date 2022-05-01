from rest_framework.routers import DefaultRouter
from .views import TechnologieItemViewSet, KeyExperienceViewSet, ExperienceViewSet

router = DefaultRouter()
router.register('expertises', ExperienceViewSet)
router.register('technologies', TechnologieItemViewSet)
router.register('keyExperiences', KeyExperienceViewSet)