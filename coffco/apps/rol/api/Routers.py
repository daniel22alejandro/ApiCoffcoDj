from django.urls import path,include
from apps.rol.api.Views import rolViewSet
from rest_framework import routers
routerRol = routers.DefaultRouter()
routerRol.register(prefix='rol',basename='rol',viewset=rolViewSet)