from django.urls import path,include
from apps.valor.api.Views import ValorViewSet
from rest_framework import routers
routerValor = routers.DefaultRouter()
routerValor.register(prefix='valor',basename='valor',viewset=ValorViewSet)