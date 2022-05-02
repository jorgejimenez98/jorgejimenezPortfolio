from rest_framework import viewsets
from .serializers import *


class Main_TechViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Main_Tech.objects.all().order_by('-proccessPorcent')
    serializer_class = Main_TechSerializer

class TechnologieItemViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = TechnologieItem.objects.all()
    serializer_class = TechnologieItemSerializer

class TechnologyViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Technologie.objects.all().order_by('-pk')
    serializer_class = TechnologieSerializer