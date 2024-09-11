from django.urls import path,include
from apps.servicio.api.Views import ServicioViewSet
from rest_framework import routers
routerServicio = routers.DefaultRouter()
routerServicio.register(prefix='servicio',basename='servicio',viewset=ServicioViewSet)
