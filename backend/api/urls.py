from rest_framework import routers
from django.conf.urls import include
from django.urls import path
from .views import getSiteConfigurations, SocialMediaViewSet

router = routers.DefaultRouter()
router.register('socialMedias', SocialMediaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('getSiteConfigurations/', getSiteConfigurations),
]
