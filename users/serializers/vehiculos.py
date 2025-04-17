from rest_framework import serializers
from users.models import Vehiculos


class VehiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculos
        fields = '__all__'
