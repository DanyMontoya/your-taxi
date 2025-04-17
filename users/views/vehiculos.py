from rest_framework import viewsets
from users.models import Vehiculos
from users.serializers import VehiculosSerializer


class VehiculosViewSet(viewsets.ModelViewSet):
    queryset = Vehiculos.objects.all()
    serializer_class = VehiculosSerializer
