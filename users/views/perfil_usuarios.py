from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from users.models import Usuarios, PerfilUsuario, MetodoPago, Viaje
from users.serializers import PerfilUsuarioSerializer, MetodoPagoSerializer, ViajeSerializer, UsuarioPerfilCompletoSerializer


class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Para que un usuario vea solo su perfil
        return PerfilUsuario.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class MetodoPagoViewSet(viewsets.ModelViewSet):
    serializer_class = MetodoPagoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MetodoPago.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ViajeViewSet(viewsets.ModelViewSet):
    serializer_class = ViajeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Viaje.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# Vista para obtener usuario con perfil completo (sin modificar)


class UsuarioPerfilCompletoAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        usuarios = request.user
        serializer = UsuarioPerfilCompletoSerializer(usuarios)
        return Response(serializer.data)
