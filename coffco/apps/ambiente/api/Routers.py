from django.urls import path,include
from apps.ambiente.api.Views import AmbienteViewSet
from rest_framework import routers
routerAmbiente = routers.DefaultRouter()
routerAmbiente.register(prefix='ambiente',basename='ambiente',viewset=AmbienteViewSet)
