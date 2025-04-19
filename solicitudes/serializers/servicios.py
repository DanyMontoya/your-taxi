from rest_framework import serializers
from solicitudes.models import Servicios


class ServiciosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicios
        fields = '__all__'


# from rest_framework import serializers
# from solicitudes.models import Servicios


# class ServiciosSerializer(serializers.ModelSerializer):
#     Usuario = serializers.SerializerMethodField()
#     Taxista = serializers.SerializerMethodField()
#     Vehiculo = serializers.SerializerMethodField()
#     tarifa = serializers.SerializerMethodField()
#     fecha_hora = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

#     class Meta:
#         model = Servicios
#         fields = ['id', 'Usuario', 'Taxista', 'Vehiculo',
#                   'fecha_hora', 'origen', 'destino', 'tarifa']

#     def get_Usuario(self, obj):
#         return f"{obj.Usuarios.nombres} ({obj.Usuarios.direccion})" if obj.Usuarios else None

#     def get_Taxista(self, obj):
#         if obj.Taxistas and obj.Taxistas.vehiculo:
#             return f"{obj.Taxistas.nombres} - {obj.Taxistas.vehiculo.placa}"
#         elif obj.Taxistas:
#             return obj.Taxistas.nombres
#         return None

#     def get_Vehiculo(self, obj):
#         return obj.Vehiculos.placa if obj.Vehiculos else None

#     def get_tarifa(self, obj):
#         # Formato de pesos colombianos sin decimales
#         return f"${int(obj.tarifa):,}".replace(",", ".")
