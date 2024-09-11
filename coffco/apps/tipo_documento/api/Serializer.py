from rest_framework.serializers import ModelSerializer
from apps.tipo_documento.models import Tipo_Documento

class Tipo_DocumentoSerializer(ModelSerializer):
    class Meta:
        model=Tipo_Documento
        fields= [
            "nombreDocumento","estado"
        ]