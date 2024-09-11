from rest_framework.serializers import ModelSerializer
from apps.logo_documento.models import LogoDocumento

class LogoDocumentoSerializer(ModelSerializer):
    class Meta:
        model = LogoDocumento
        fields = [ 'logo', 'documento']
