from rest_framework import viewsets
from solicitudes.models import Calificaciones
from solicitudes.serializers import CalificacionesSerializers


class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificaciones.objects.all()  # pylint: disable=no-member
    serializer_class = CalificacionesSerializers

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from solicitudes.models import Calificaciones, Servicios
# from users.models import Taxistas, Usuarios
# from solicitudes.serializers import CalificacionesSerializers
# from rest_framework import permissions


# class CrearCalificacionAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         data = request.data
#         servicio_id = data.get('servicio')

#         try:
#             servicio = Servicios.objects.get(id=servicio_id)
#         except Servicios.DoesNotExist:
#             return Response({'error': 'Servicio no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

#         # Verificar si ya existe calificación para ese servicio
#         calificacion, created = Calificaciones.objects.get_or_create(
#             servicio=servicio)

#         # Validar si quien califica es usuario
#         if Usuarios.objects.filter(usuario=user).exists():
#             if calificacion.calificacion_usuario_a_taxista is not None:
#                 return Response({'error': 'Ya calificaste a este taxista en este servicio.'}, status=status.HTTP_400_BAD_REQUEST)
#             calificacion.calificacion_usuario_a_taxista = data.get(
#                 'calificacion_usuario_a_taxista')
#             calificacion.save()
#             serializer = CalificacionesSerializers(calificacion)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         # Validar si quien califica es taxista
#         elif Taxistas.objects.filter(usuario=user).exists():
#             if calificacion.calificacion_taxista_a_usuario is not None:
#                 return Response({'error': 'Ya calificaste a este usuario en este servicio.'}, status=status.HTTP_400_BAD_REQUEST)
#             calificacion.calificacion_taxista_a_usuario = data.get(
#                 'calificacion_taxista_a_usuario')
#             calificacion.save()
#             serializer = CalificacionesSerializers(calificacion)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response({'error': 'No tienes permiso para calificar este servicio.'}, status=status.HTTP_403_FORBIDDEN)
