from rest_framework import viewsets
from .models import ResourceTourist
from .serializers import ResourceTouristSerializer


class ResourceTouristViewSet(viewsets.ModelViewSet):

    queryset = ResourceTourist.objects.all()
    serializer_class = ResourceTouristSerializer