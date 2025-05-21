from django.contrib import admin
from users.models import Usuarios


@admin.register(Usuarios)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombres', 'primer_apellido',
                    'telefono', 'is_active')
    list_filter = ('genero', 'is_active')
    search_fields = ('email', 'nombres', 'primer_apellido', 'documento')
