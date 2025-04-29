from rest_framework import serializers
from solicitudes.models import Servicios


class ServiciosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicios
        fields = '__all__'
