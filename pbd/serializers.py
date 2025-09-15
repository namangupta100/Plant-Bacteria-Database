from rest_framework import serializers
from .models import PlantProbioticBacteria

class PlantProbioticBacteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantProbioticBacteria
        fields = ['id', 'genus', 'species', 'strain', 'plant_host', 'function', 'mode_of_action', 'reference', 'created_at', 'updated_at']
