from django.urls import path,include
from apps.documentos.api.Views import DocumetoViewset
from rest_framework import routers
routerDocumento = routers.DefaultRouter()
routerDocumento.register(prefix='documentos',basename='documentos',viewset=DocumetoViewset)