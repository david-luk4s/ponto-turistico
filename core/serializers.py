from rest_framework import serializers
from .models import TouristPoint
from resource_tourist.serializers import ResourceTouristSerializer
from location.serializers import LocationSerializer


class TouristPointSerializer(serializers.ModelSerializer):
    resource_tourists = ResourceTouristSerializer(many=True)
    location = LocationSerializer()
    complet_description = serializers.SerializerMethodField()

    class Meta:
        model = TouristPoint
        fields = ('pk', 'name', 'description', 'photo', 'location', 
        'resource_tourists', 'complet_description', 'complet_description_two')
    
    def get_complet_description(self, instance):
        return f'{instance.name} - {instance.description}'