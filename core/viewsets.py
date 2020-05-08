from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import TouristPoint
from .serializers import TouristPointSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TouristPointViewSet(viewsets.ModelViewSet):
    serializer_class = TouristPointSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'description']
    search_fields = ['name', 'description']
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        pass


    def get_queryset(self):
        return TouristPoint.objects.all()


    def list(self, request, *args, **kwargs):
        return super(TouristPointViewSet, self).list(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        return super(TouristPointViewSet, self).create(request, *args, **kwargs)


    def destroy(self, request, *args, **kwargs):
        return super(TouristPointViewSet, self).destroy(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        return super(TouristPointViewSet, self).update(request, *args, **kwargs)


    def partial_update(self, request, *args, **kwargs):
        return super(TouristPointViewSet, self).partial_update(request, *args, **kwargs)


    @action(methods=['get'], detail=True) # -> detail: True receive pk, detail: False resource not pk
    def baterponto(self, request, pk):
        return Response({'Recurso bater ponto: ': pk})
