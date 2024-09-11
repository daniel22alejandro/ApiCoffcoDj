from rest_framework import viewsets
from apps.servicio.models import Servicio
from apps.servicio.api.Serializers import ServicioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
