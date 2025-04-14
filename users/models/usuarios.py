from django.db import models


class Usuarios(models.Model):
    identificacion = models.CharField(max_length=45)
    nombres = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250, null=True)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20, null=True)
    telefono = models.CharField(max_length=30, null=True)
    correo = models.EmailField(max_length=50, null=True)

    def __str__(self):
        return self.nombres
