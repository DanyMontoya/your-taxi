# para registrar mis modelos.
# from django.contrib import admin
# from .models import Usuarios


# class UsuarioAdmin(admin.ModelAdmin):
#     # Aquí puedo personalizar la forma en que se muestran los usuarios en el admin
#     list_display = list_display = (
#         'username', 'correo', 'telefono')  # Campos a mostrar
#     search_fields = ('email', 'nombres')  # Campos por los que se puede buscar
#     list_filter = ('genero', 'fecha_nacimiento')  # Filtros disponibles
#     # ordering = ('-date_joined',)  # Orden por fecha de creación


# admin.site.register(Usuarios, UsuarioAdmin)

from django.contrib import admin
from users.models import Usuarios


@admin.register(Usuarios)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('correo', 'nombres', 'primer_apellido',
                    'telefono', 'is_active')
    list_filter = ('genero', 'is_active')
    search_fields = ('correo', 'nombres', 'primer_apellido', 'documento')
