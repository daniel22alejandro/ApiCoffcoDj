from django.urls import path,include
from apps.tipo_servicios.api.Views import TipoServicioViewSet
from rest_framework import routers
routerTipoServicio = routers.DefaultRouter()
routerTipoServicio.register(prefix='tipo_servicio',basename='tipo_servicio',viewset=TipoServicioViewSet)
