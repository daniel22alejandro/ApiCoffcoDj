from rest_framework.serializers import ModelSerializer
from apps.variables.models import VariblesModel

class VariableSerializer(ModelSerializer):
    class Meta:
        model=VariblesModel
        fields=[
            "nombreVaribles","estadovarible","tipo_Dato"
        ]
