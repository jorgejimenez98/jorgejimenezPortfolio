from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .helpers import send_email_to_user, send_email_to_me


@api_view(['GET'])
@permission_classes([AllowAny])
def getSiteConfigurations(request):
    from .models import SiteConfiguration
    from .serializers import SiteConfigurationSerializer
    try:
        config = SiteConfiguration.objects.get()
        serializer = SiteConfigurationSerializer(
            config, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def sendEmail(request):
    import os
    try:
        send_email_to_user(request.data, os.environ.get('EMAIL_HOST_USER'))
        send_email_to_me(request.data)
        return Response({"message": "Email Sended Successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"detail": e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
