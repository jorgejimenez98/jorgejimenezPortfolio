from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *


""" Technology View Set """


class Main_TechViewSet(viewsets.ModelViewSet):
    queryset = Main_Tech.objects.all().order_by('-pk')
    serializer_class = Main_TechSerializer


class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technologie.objects.all().order_by('-pk')
    serializer_class = TechnologieSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            """ Create New Tech """
            newTech = Technologie.objects.create(
                name=data.get('name'),
                image_logo=data.get('image_logo'),
            )
            """ Save Image FIle """
            fs = FileSystemStorage()
            fs.save(newTech.image_logo.name, data.get('image_logo'))
            """ Return Response """
            return Response(TechnologieSerializer(newTech).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
