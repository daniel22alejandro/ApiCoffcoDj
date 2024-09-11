from django.urls import path,include
from apps.logo_documento.api.Views import LogoDocumentoViewSet
from rest_framework import routers
routerLogoDocumento = routers.DefaultRouter()
routerLogoDocumento.register(prefix='logo_documento',basename='logo_documento',viewset=LogoDocumentoViewSet)