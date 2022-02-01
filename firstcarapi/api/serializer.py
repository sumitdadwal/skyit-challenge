from rest_framework import serializers
from firstcarapi.models import Car, UpdatedMileage

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['unit', 'mileage', 'manufacturer', 'status']

class UpdatedMileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdatedMileage
        fields = ['updated_unit', 'created_at']