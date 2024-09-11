from rest_framework.serializers import ModelSerializer
from apps.tipo_servicios.models import TipoServicio

class TipoServicioSerializer(ModelSerializer):
    class Meta:
        model = TipoServicio
        fields = ['nombreServicio', 'estado']
