from rest_framework import viewsets
from .serializers import *

class KeyExperienceViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = KeyExperience.objects.all()
    serializer_class = KeyExperienceSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Experience.objects.all().order_by('-date_end')
    serializer_class = ExperienceSerializer