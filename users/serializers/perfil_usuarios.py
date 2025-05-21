from rest_framework import serializers
from users.models import Usuarios, PerfilUsuario, MetodoPago, Viaje
# from users.models import Usuarios


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ['id', 'direccion', 'preferencias']


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['id', 'tipo', 'detalles', 'activo', 'creado']


class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = ['id', 'origen', 'destino', 'fecha_solicitud', 'fecha_inicio',
                  'fecha_fin', 'costo', 'estado', 'taxista', 'vehiculo']

# este es el serializer que incluya perfil, métodos de pago y viajes en un solo lugar


class UsuarioPerfilCompletoSerializer(serializers.ModelSerializer):
    perfil = PerfilUsuarioSerializer(read_only=True)
    metodos_pago = MetodoPagoSerializer(many=True, read_only=True)
    viajes = ViajeSerializer(many=True, read_only=True)

    class Meta:
        model = Usuarios
        fields = [
            'id', 'email', 'username', 'nombres', 'primer_apellido', 'segundo_apellido', 'documento',
            'perfil', 'metodos_pago', 'viajes', 'telefono'
        ]
