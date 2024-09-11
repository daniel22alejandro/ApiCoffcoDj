from django.urls import path,include
from apps.variables.api.views import variablesViewSet
from rest_framework import routers
routerVariable = routers.DefaultRouter()
routerVariable.register(prefix='variables',basename='variables',viewset=variablesViewSet)