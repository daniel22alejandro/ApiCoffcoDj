from django.db import models
from apps.versiones.models import Versione
from apps.variables.models import VariblesModel
from django.db.models import SET_NULL

class Detalle(models.Model):
    versiones=models.ForeignKey(Versione,on_delete=SET_NULL,null=True,blank=True)
    variables=models.ForeignKey(VariblesModel,on_delete=SET_NULL,null=True, blank=True)
    def __str__(self):
        return str(self.versiones)