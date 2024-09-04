from rest_framework.serializers import ModelSerializer
from apps.rol.models import RolModels


class RolSerializers(ModelSerializer):
    class Meta:
        model=RolModels
        fields=['rol']