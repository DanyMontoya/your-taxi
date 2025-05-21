# from rest_framework import serializers
# from users.models import Usuarios


# class UsuariosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuarios
#         fields = '__all__'


# from django.core.exceptions import ValidationError
# from django.core.validators import MinLengthValidator
# from rest_framework import serializers
# from users.models import Usuarios


# class UsuarioSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         # write_only=True, validators=[MinLengthValidator(5)])
#         write_only=True, validators=[MinLengthValidator(6)])

#     class Meta:
#         model = Usuarios
#         fields = [
#             'id', 'tipo_documento', 'documento', 'primer_apellido', 'segundo_apellido', 'nombres',
#             'genero', 'fecha_nacimiento', 'email', 'telefono', 'username', 'password'
#         ]

#     # def validate_correo(self, value):
#     #     """Validación para asegurar que el correo no esté en uso."""
#     #     if Usuarios.objects.filter(correo=value).exists():
#     #         raise ValidationError("El correo electrónico ya está en uso.")
#     #     return value

#         def create(self, validated_data):
#             """Crea un nuevo usuario y guarda la contraseña de manera segura."""
#             password = validated_data.pop('password')
#             user = Usuarios(**validated_data)
#             user.set_password(password)
#             user.save()
#             return user

from django.core.validators import MinLengthValidator
from rest_framework import serializers
from users.models import Usuarios


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, validators=[MinLengthValidator(6)]
    )

    class Meta:
        model = Usuarios
        fields = [
            'id', 'tipo_documento', 'documento', 'primer_apellido', 'segundo_apellido', 'nombres',
            'genero', 'fecha_nacimiento', 'email', 'telefono', 'username', 'password'
        ]

    def create(self, validated_data):
        """Crea un nuevo usuario y guarda la contraseña de manera segura."""
        password = validated_data.pop('password')
        user = Usuarios(**validated_data)
        user.set_password(password)
        user.save()
        return user
