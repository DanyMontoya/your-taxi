# from rest_framework import serializers
# from users.models import Taxistas


# class TaxistasSerializer(serializers.ModelSerializer):
#     vehiculo = serializers.StringRelatedField()

#     class Meta:
#         model = Taxistas
#         fields = '__all__'

from rest_framework import serializers
from users.models import Taxistas, Vehiculos


class TaxistasSerializer(serializers.ModelSerializer):
    placa = serializers.StringRelatedField(
        source='vehiculo', read_only=True)  # muestra la placa como campo extra
    vehiculo = serializers.PrimaryKeyRelatedField(
        queryset=Vehiculos.objects.all())  # permite modificar por ID

    class Meta:
        model = Taxistas
        fields = ['id', 'nombres', 'numero_licencia',
                  'telefono', 'vehiculo', 'placa']
