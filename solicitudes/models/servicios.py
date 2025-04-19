from django.db import models


class Servicios(models.Model):
    Usuarios = models.ForeignKey(
        'users.Usuarios', on_delete=models.SET_NULL, null=True)
    Taxistas = models.ForeignKey(
        'users.Taxistas', on_delete=models.SET_NULL, null=True)
    Vehiculos = models.ForeignKey(
        'users.Vehiculos', on_delete=models.SET_NULL, null=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    tarifa = models.IntegerField()

    def __str__(self):
        return f"Servicio de {self.origen} a {self.destino}"
