from django.db import models
from apps.servicios.models import ServicioModels
from apps.tipo_servicios.models import TipoServicio
from django.db.models import SET_NULL
class PreciosModels(models.Model):
    ESTADO_CHOICES=[
        ('activo','activo'),
        ('inactivo','inactivo')
    ]
    presentacion =models.CharField(max_length=100)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2 
    )
    tipoServicio=models.ForeignKey(TipoServicio,on_delete=SET_NULL,null=True,blank=True)
    servicio=models.ForeignKey(ServicioModels,on_delete=SET_NULL,null=True,blank=True)
    estado= models.CharField(max_length=30, choices=ESTADO_CHOICES, default='activo')
    