from rest_framework import serializers
from .models import Succulent

class SucculentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Succulent
        fields = ['id', 'name', 'succulent_type', 'importedFrom', 'buyingPrice', 'sellingPrice']

    def create(self,validated_data):
        return Succulent.objects.create(**validated_data)
