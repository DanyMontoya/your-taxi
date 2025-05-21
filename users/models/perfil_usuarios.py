from django.db import models
# para referenciar el modelo usuario personalizado
from django.conf import settings


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil')
    direccion = models.CharField(max_length=255, blank=True)
    # con esto guardo preferencias flexibles
    preferencias = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.email}"


class MetodoPago(models.Model):
    TIPO_CHOICES = [
        ('credito', 'Tarjeta de Crédito'),
        ('debito', 'Tarjeta Débito'),
        ('efectivo', 'Efectivo'),
        ('nequi', 'Nequi'),
        ('daviplata', 'Daviplata'),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='metodos_pago')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    detalles = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} ({self.usuario.email})"


class Viaje(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='viajes')
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    costo = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)
    # ejejemplo: pendiente, en_curso, finalizado, cancelado
    estado = models.CharField(max_length=50, default='pendiente')
    taxista = models.ForeignKey(
        'users.Taxistas', on_delete=models.SET_NULL, null=True, blank=True)
    vehiculo = models.ForeignKey(
        'users.Vehiculos', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Viaje {self.id} de {self.usuario.email} - {self.origen} a {self.destino}"
