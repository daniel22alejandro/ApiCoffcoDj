from rest_framework import viewsets
from apps.variables.models import VariblesModel
from apps.variables.api.Serializer import VariableSerializer

class variablesView(viewsets.ModelViewSet):
    serializer_class = VariableSerializer
    queryset = VariblesModel.objects.all()