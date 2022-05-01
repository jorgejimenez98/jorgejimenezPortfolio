from rest_framework import viewsets
from .serializers import *

class TechnologieItemViewSet(viewsets.ModelViewSet):
    queryset = TechnologieItem.objects.all()
    serializer_class = TechnologieItemSerializer

class KeyExperienceViewSet(viewsets.ModelViewSet):
    queryset = KeyExperience.objects.all()
    serializer_class = KeyExperienceSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer