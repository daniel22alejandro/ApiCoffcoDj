from rest_framework.serializers import ModelSerializer
from apps.servicio.models import Servicio

class ServicioSerializer(ModelSerializer):
    class Meta:
        model = Servicio
        fields = [
            'nombre', 
            'tipo_servicio', 
            'fecha', 
            'ambiente', 
            'muestra', 
            'usuario', 
            'estado', 
            'fecha_inicio', 
            'fecha_fin'
        ]
