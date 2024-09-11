from django.urls import path,include
from apps.muestra.api.View import MuestraViewSet
from rest_framework import routers
routerMuestra = routers.DefaultRouter()
routerMuestra.register(prefix='muestra',basename='muestra',viewset=MuestraViewSet)