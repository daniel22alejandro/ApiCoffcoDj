from rest_framework import viewsets
from apps.logos.models import Logo
from apps.logos.api.Serializers import LogoSerializer

class LogoViewSet(viewsets.ModelViewSet):
    serializer_class = LogoSerializer
    queryset = Logo.objects.all()
