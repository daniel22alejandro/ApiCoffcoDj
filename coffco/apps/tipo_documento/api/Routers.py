from django.urls import path,include
from apps.tipo_documento.api.Views import TipoDocumentoViewSet
from rest_framework import routers
routerTipoDocumento = routers.DefaultRouter()
routerTipoDocumento.register(prefix='tipo_documento',basename='tipo_documento',viewset=TipoDocumentoViewSet)
