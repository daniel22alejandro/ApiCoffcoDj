from rest_framework.serializers import  ModelSerializer
from apps.servicios.models import ServicioModels

class ServicioSerializers(ModelSerializer):
    class Meta:
        model = ServicioModels
        fields = ['nombre_servicio','versiones', 'muestra']

