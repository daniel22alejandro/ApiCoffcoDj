from django.db import models
from apps.muestra.models import Muestra
from apps.tipo_servicios.models import TipoServicio  
from apps.ambiente.models import Ambiente                   
from apps.user.models import User          
from django.db.models import SET_NULL

class Servicio(models.Model):
    nombre = models.CharField(max_length=45, null=True, blank=True) 
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=SET_NULL, null=True, blank=True)  
    fecha = models.DateField(null=True, blank=True)  # Campo fecha
    ambiente = models.ForeignKey(Ambiente, on_delete=SET_NULL, null=True, blank=True)  
    muestra = models.ForeignKey(Muestra, on_delete=SET_NULL, null=True, blank=True)   
    usuario = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True) 
    estado = models.CharField(max_length=8, choices=[('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')  
    fecha_inicio = models.DateField(null=True, blank=True)  
    fecha_fin = models.DateField(null=True, blank=True)  

    def __str__(self):
        return self.nombre
