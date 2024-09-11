from rest_framework import viewsets
from apps.ambiente.models import Ambiente
from apps.ambiente.api.Serializers import AmbienteSerializer

class AmbienteViewSet(viewsets.ModelViewSet):
    serializer_class = AmbienteSerializer
    queryset = Ambiente.objects.all()
