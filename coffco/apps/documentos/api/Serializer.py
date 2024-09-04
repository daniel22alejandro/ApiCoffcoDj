from rest_framework.serializers import  ModelSerializer
from apps.documentos.models import Documento

class documentosSerializer(ModelSerializer):
    class Meta:
        model = Documento
        fields = ['nombre',
                  'fecha_carga',
                    'descripcion',
                    'codigo_documento',
                    'fecha_Emision',
                    'fk_tipoServicio',
                    'fkTipoDocumentos']

