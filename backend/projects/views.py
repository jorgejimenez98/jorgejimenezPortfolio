from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectMiniSerializer

    def retrieve(self, request, pk=None):
        serializer = ProjectSerializer(self.get_object(), context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)