from django.db import models


class Taxistas(models.Model):
    nombres = models.CharField(max_length=150)
    numero_licencia = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    # vehiculo = models.ForeignKey('Vehiculos', on_delete=models.PROTECT)
    vehiculo = models.ForeignKey(
        'Vehiculos', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombres} - {self.vehiculo.placa}"

    # def __str__(self):
    # return f"{self.nombres} - {self.vehiculo.placa if self.vehiculo else 'Sin vehículo'}"
