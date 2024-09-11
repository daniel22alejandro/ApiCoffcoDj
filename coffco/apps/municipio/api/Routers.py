from django.urls import path,include
from apps.municipio.api.Views import MunicipioViewSet
from rest_framework import routers
routerMunicipio = routers.DefaultRouter()
routerMunicipio.register(prefix='municipio',basename='municipio',viewset=MunicipioViewSet)