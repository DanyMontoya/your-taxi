from django.db import models


class Vehiculos(models.Model):
    placa = models.CharField(max_length=15)
    modelo = models.IntegerField()
    marca = models.CharField(max_length=30)

    def __str__(self):
        # return f"{self.marca} {self.modelo} ({self.placa})"
        return self.placa
