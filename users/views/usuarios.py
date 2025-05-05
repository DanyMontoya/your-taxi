# from rest_framework import viewsets
# from users.models import Usuarios
# from users.serializers import UsuarioSerializer


# class RegistroUsuarioView(viewsets.ModelViewSet):
#     queryset = Usuarios.objects.all()
#     serializer_class = UsuarioSerializer

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework import generics
# from users.models import Usuarios
# from users.serializers import UsuarioSerializer
# from rest_framework.exceptions import ValidationError


# class RegistroUsuarioView(generics.CreateAPIView):
#     queryset = Usuarios.objects.all()
#     serializer_class = UsuarioSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if not serializer.is_valid():
#             # Muestra en consola los errores concretos
#             print("Errores de validación:", serializer.errors)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         self.perform_create(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class RegistroUsuarioView(generics.CreateAPIView):
#     queryset = Usuarios.objects.all()
#     serializer_class = UsuarioSerializer

#     def create(self, request, *args, **kwargs):
#         # Verificar si el correo ya existe
#         correo = request.data.get('correo')
#         if Usuarios.objects.filter(correo=correo).exists():
#             raise ValidationError(
#                 {"correo": "El correo electrónico ya está registrado."})

#         return super().create(request, *args, **kwargs)


from rest_framework import viewsets
from users.models import Usuarios
from users.serializers import UsuarioSerializer
from rest_framework.exceptions import ValidationError


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        correo = request.data.get('correo')
        if Usuarios.objects.filter(correo=correo).exists():
            raise ValidationError(
                {"correo": "El correo electrónico ya está registrado."})
        return super().create(request, *args, **kwargs)
