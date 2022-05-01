from rest_framework.routers import DefaultRouter
from .views import SocialMediaViewSet, CurriculumViewSet 

router = DefaultRouter()
router.register('curriculums', CurriculumViewSet)
router.register('social_medias', SocialMediaViewSet)