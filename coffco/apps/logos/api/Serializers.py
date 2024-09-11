from rest_framework.serializers import ModelSerializer
from apps.logos.models import Logo

class LogoSerializer(ModelSerializer):
    class Meta:
        model = Logo
        fields = ['ruta', 'estado', 'nombre']
