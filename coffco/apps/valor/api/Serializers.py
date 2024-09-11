from rest_framework.serializers import ModelSerializer
from apps.valor.models import Valor

class ValorSerializer(ModelSerializer):
    class Meta:
        model = Valor
        fields = [ 'fk_id_servicio', 'fk_id_detalle', 'valor']
