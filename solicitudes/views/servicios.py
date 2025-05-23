from rest_framework import viewsets
from solicitudes.models import Servicios
from solicitudes.serializers import ServiciosSerializer
from users.models import Taxistas, Vehiculos


class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()  # pylint: disable=no-member
    serializer_class = ServiciosSerializer

    def perform_create(self, serializer):
        taxista = serializer.validated_data['Taxistas']
        vehiculo = taxista.vehiculo
        serializer.save(Vehiculos=vehiculo)
