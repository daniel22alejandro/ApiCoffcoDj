from rest_framework import viewsets
from apps.tipo_documento.models import Tipo_Documento
from apps.tipo_documento.api.Serializer import Tipo_DocumentoSerializer

class TipoDocumentoViewsts(viewsets.ModelViewSet):
    serializer_class=Tipo_DocumentoSerializer
    queryset=Tipo_Documento.objects.all()
    