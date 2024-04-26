from rest_framework import serializers
from .models import Cars

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'name', 'description', 'buyingPrice', 'sellingPrice', 'sellingPrice', "createdAt", "ownerId", "carImg"]

    def create(self,validated_data):
        return Cars.objects.create(**validated_data)
