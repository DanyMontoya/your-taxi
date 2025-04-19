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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UsuariosViewset, TaxistasViewSet, VehiculosViewSet
from solicitudes.views import ServiciosViewSet
router = DefaultRouter()
router.register('usuarios', UsuariosViewset, 'view_usuarios')
router.register('taxistas', TaxistasViewSet, 'view_taxistas')
router.register('vehiculos', VehiculosViewSet, 'view_vehiculos')
router.register('servicios', ServiciosViewSet, 'view_servicios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
