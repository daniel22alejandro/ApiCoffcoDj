# apps/valor/models.py
from django.db import models
from apps.servicio.models import Servicio
from apps.detalle.models import Detalle

class Valor(models.Model):
    fk_id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fk_id_detalle = models.ForeignKey(Detalle, on_delete=models.CASCADE)
    valor = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.valor
