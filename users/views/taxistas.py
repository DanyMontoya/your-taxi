from rest_framework import viewsets
from users.models import Taxistas
from users.serializers import TaxistasSerializer


class TaxistasViewSet(viewsets.ModelViewSet):
    queryset = Taxistas.objects.all()
    serializer_class = TaxistasSerializer
