from rest_framework import serializers
from solicitudes.models import Calificaciones


class CalificacionesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Calificaciones
        fields = '__all__'


# class CalificacionSerializer(serializers.ModelSerializer):
#     nombre_usuario = serializers.SerializerMethodField()
#     nombre_taxista = serializers.SerializerMethodField()

#     class Meta:
#         model = Calificacion
#         fields = [
#             'id',
#             'servicio',
#             'nombre_usuario',
#             'nombre_taxista',
#             'calificacion_usuario_a_taxista',
#             'comentario_usuario_a_taxista',
#             'fecha_usuario',
#             'calificacion_taxista_a_usuario',
#             'comentario_taxista_a_usuario',
#             'fecha_taxista',
#         ]

#     def get_nombre_usuario(self, obj):
#         return obj.servicio.usuarios.nombre if obj.servicio.usuarios else None

#     def get_nombre_taxista(self, obj):
#         return obj.servicio.taxistas.nombre if obj.servicio.taxistas else None

#     def validate(self, data):
#         for campo in ['calificacion_usuario_a_taxista', 'calificacion_taxista_a_usuario']:
#             if campo in data and data[campo] is not None:
#                 if data[campo] < 1 or data[campo] > 5:
#                     raise serializers.ValidationError({campo: "La calificación debe estar entre 1 y 5."})
#         return data
