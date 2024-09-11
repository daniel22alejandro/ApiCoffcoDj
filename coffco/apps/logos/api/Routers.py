from django.urls import path,include
from apps.logos.api.Views import LogoViewSet
from rest_framework import routers
routerLogo = routers.DefaultRouter()
routerLogo.register(prefix='logo',basename='logo',viewset=LogoViewSet)
