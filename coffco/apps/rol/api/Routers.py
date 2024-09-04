from django.urls import path,include
from apps.rol.api.Views import rolViews
from rest_framework import routers
routerRol = routers.DefaultRouter()
routerRol.register(prefix='rol',basename='rol',viewset=rolViews)