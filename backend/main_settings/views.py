from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import SiteConfiguration
from .serializers import SiteConfigurationSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def getSiteConfigurations(request):
    try:
        config = SiteConfiguration.objects.get()
        serializer = SiteConfigurationSerializer(config, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)