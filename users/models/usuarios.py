from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UsuarioManager(BaseUserManager):
    """Gestor personalizado de usuarios."""

    def create_user(self, email, password=None, **extra_fields):
        """Crea y retorna un usuario con correo y contraseña."""
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Crea y retorna un superusuario con privilegios de administrador."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Usuarios(AbstractBaseUser, PermissionsMixin):
    tipo_documento = models.CharField(max_length=40)
    documento = models.CharField(max_length=20, unique=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True)
    nombres = models.CharField(max_length=100)
    genero = models.CharField(max_length=15, null=True)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['username', 'documento']

    def __str__(self):
        return f"{self.nombres} ({self.correo})"
