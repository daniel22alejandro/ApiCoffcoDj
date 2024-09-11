
from rest_framework import viewsets
from apps.documentos.models import Documento
from apps.documentos.api.Serializer import documentosSerializer
from apps.documentos.api.permissions import IsAdmin
class DocumetoViewset(viewsets.ModelViewSet):
    permission_classes=[IsAdmin]
    serializer_class = documentosSerializer
    queryset = Documento.objects.all()