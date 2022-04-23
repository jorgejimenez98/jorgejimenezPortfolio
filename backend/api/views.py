from django.core.files.storage import FileSystemStorage
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *


""" Social Media View Set """


class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all().order_by('-pk')
    serializer_class = SocialMediaSerializer


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


""" Curriculum View Set """


class CurriculumViewSet(viewsets.ModelViewSet):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer


""" Projects """


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectMiniSerializer

    def retrieve(self, request, pk=None):
        serializer = ProjectSerializer(self.get_object(), context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


""" Experiences """

class TechnologieItemViewSet(viewsets.ModelViewSet):
    queryset = TechnologieItem.objects.all()
    serializer_class = TechnologieItemSerializer

class KeyExperienceViewSet(viewsets.ModelViewSet):
    queryset = KeyExperience.objects.all()
    serializer_class = KeyExperienceSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer