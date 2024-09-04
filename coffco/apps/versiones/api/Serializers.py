from rest_framework.serializers import  ModelSerializer
from apps.versiones.models import Versione

class VersioneSerializers(ModelSerializer):
    class Meta:
        model = Versione
        fields = ['version','documento','estado','nombre_documento','fecha_version']

