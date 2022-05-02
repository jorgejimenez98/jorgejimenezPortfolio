from rest_framework import viewsets
from .serializers import *


class Main_TechViewSet(viewsets.ModelViewSet):
    queryset = Main_Tech.objects.all().order_by('-pk')
    serializer_class = Main_TechSerializer

class TechnologieItemViewSet(viewsets.ModelViewSet):
    queryset = TechnologieItem.objects.all()
    serializer_class = TechnologieItemSerializer

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technologie.objects.all().order_by('-pk')
    serializer_class = TechnologieSerializer