"""
URL configuration for your_taxi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from solicitudes.views import ServiciosViewSet, CalificacionViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import (
    UsuariosViewSet, TaxistasViewSet, VehiculosViewSet, PerfilUsuarioViewSet,
    MetodoPagoViewSet, ViajeViewSet, UsuarioPerfilCompletoAPIView, LoginView,
)
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('taxistas', TaxistasViewSet, basename='taxistas')
router.register('vehiculos', VehiculosViewSet, basename='vehiculos')
router.register('servicios', ServiciosViewSet, basename='servicios')
router.register('usuarios', UsuariosViewSet, basename='usuarios')
router.register('calificaciones', CalificacionViewSet,
                basename='calificaciones')
router.register('perfil', PerfilUsuarioViewSet, basename='perfil')
router.register('metodos-pago', MetodoPagoViewSet, basename='metodospago')
router.register('viajes', ViajeViewSet, basename='viajes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # Para login con token (opcional, si uso TokenAuthentication)
    path('api/login-token/', obtain_auth_token, name='api_token_auth'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('usuario/perfil-completo/', UsuarioPerfilCompletoAPIView.as_view(),
         name='usuario-perfil-completo'),
]
