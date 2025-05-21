# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token


# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         if not email or not password:
#             return Response({'error': 'Email y contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

#         user = authenticate(request, email=email, password=password)
#         if not user:
#             return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)

#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email y contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)
        if not user:
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)

        # estos son los campos de mi modelo 'Usuarios'
        return Response({
            'token': token.key,
            'usuario': {
                'id': user.id,
                'nombres': user.nombres,
                'primer_apellido': user.primer_apellido,
                'segundo_apellido': user.segundo_apellido,
                'email': user.email,
                'telefono': user.telefono,
                'documento': user.documento,
                'tipo_documento': user.tipo_documento,
                'genero': user.genero,
                'fecha_nacimiento': user.fecha_nacimiento,
                'username': user.username,
            }
        })
