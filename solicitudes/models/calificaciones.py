from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Calificaciones(models.Model):
    Servicios = models.OneToOneField('Servicios', on_delete=models.CASCADE)
    calificacion_usuario_a_taxista = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    comentarios_usaurio_a_taxista = models.TextField(blank=True, null=True)

    calificacion_taxista_a_usuario = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    comentarios_taxistas_a_usuarios = models.TextField(blank=True, null=True)

    fecha_usuario = models.DateTimeField(null=True, blank=True)
    fecha_taxista = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"calificacion del servicio {self.Servicios.id}"
