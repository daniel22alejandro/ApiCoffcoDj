from rest_framework import viewsets
from apps.logo_documento.models import LogoDocumento
from apps.logo_documento.api.Serializers import LogoDocumentoSerializer

class LogoDocumentoViewSet(viewsets.ModelViewSet):
    serializer_class = LogoDocumentoSerializer
    queryset = LogoDocumento.objects.all()
