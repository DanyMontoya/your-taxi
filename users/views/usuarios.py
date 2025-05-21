from rest_framework import viewsets
from users.models import Usuarios
from users.serializers import UsuarioSerializer
from rest_framework.exceptions import ValidationError


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if Usuarios.objects.filter(email=email).exists():
            raise ValidationError(
                {"email": "El email ya está registrado."})
        return super().create(request, *args, **kwargs)
