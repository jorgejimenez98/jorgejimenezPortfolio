from rest_framework.routers import DefaultRouter
from .views import ExperienceViewSet, KeyExperienceViewSet

router = DefaultRouter()
router.register('expertises', ExperienceViewSet)
router.register('key_expertises', KeyExperienceViewSet)