from rest_framework import viewsets
from users.models import Usuarios
from users.serializers import UsuariosSerializer


class UsuariosViewset(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
