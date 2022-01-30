from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import *

""" Site Configuration View """


@api_view(['GET'])
@permission_classes([AllowAny])
def getSiteConfigurations(request):
    try:
        config = SiteConfiguration.objects.get()
        serializer = SiteConfigurationSerializer(config)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


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
