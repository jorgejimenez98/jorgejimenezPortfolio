from rest_framework.routers import DefaultRouter
from .views import Main_TechViewSet, TechnologyViewSet, TechnologieItemViewSet

router = DefaultRouter()
router.register('main_techs', Main_TechViewSet)
router.register('technologies', TechnologieItemViewSet)
router.register('technologies', TechnologyViewSet)