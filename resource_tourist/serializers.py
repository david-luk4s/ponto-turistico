from rest_framework import serializers
from .models import ResourceTourist


class ResourceTouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceTourist
        fields = ['pk', 'name', 'description', 'time_func', 'photo']
