from rest_framework import viewsets
from apps.precios.models import PreciosModels
from apps.precios.api.Serializers import PrecioSerializers

class PreciosViewSet(viewsets.ModelViewSet):
    serializer_class=PrecioSerializers
    queryset=PreciosModels.objects.all()