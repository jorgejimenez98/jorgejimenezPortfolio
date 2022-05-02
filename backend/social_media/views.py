from rest_framework import viewsets
from .serializers import *

class SocialMediaViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = SocialMedia.objects.all().order_by('-pk')
    serializer_class = SocialMediaSerializer

class CurriculumViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
