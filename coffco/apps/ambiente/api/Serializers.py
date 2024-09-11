from rest_framework.serializers import ModelSerializer
from apps.ambiente.models import Ambiente

class AmbienteSerializer(ModelSerializer):
    class Meta:
        model = Ambiente
        fields = ['nombre_ambiente', 'estado']
