from rest_framework import viewsets
from apps.valor.models import Valor
from apps.valor.api.Serializers import ValorSerializer

class ValorViewSet(viewsets.ModelViewSet):
    serializer_class = ValorSerializer
    queryset = Valor.objects.all()
