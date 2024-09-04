from rest_framework.serializers import ModelSerializer
from apps.precios.models import PreciosModels

class PrecioSerializers(ModelSerializer):
    class Meta:
        model=PreciosModels
        fields=['presentacion','precio','tipoServicio','servicio','estado']