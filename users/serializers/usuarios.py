from rest_framework import serializers
from users.models import Usuarios  # Asegúrate de usar la clase con mayúscula


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
