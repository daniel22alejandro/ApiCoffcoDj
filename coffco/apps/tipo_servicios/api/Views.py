from rest_framework import viewsets
from apps.tipo_servicios.models import TipoServicio
from apps.tipo_servicios.api.Serializers import TipoServicioSerializer

class TipoServicioViewSet(viewsets.ModelViewSet):
    queryset = TipoServicio.objects.all()
    serializer_class = TipoServicioSerializer
