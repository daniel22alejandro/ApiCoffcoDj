from django.db import models
from django.db.models import SET_NULL
from apps.documentos.models import Documento
class Versione(models.Model):
    version = models.CharField(max_length=100)
    documento=models.ForeignKey(Documento,on_delete=SET_NULL,null=True,blank=True)
    ESTADO_CHOICES=[
        ('activo','activo'),
        ('inactivo','inactivo')
    ]
    estado= models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    nombre_documento =models.FileField(null=True,blank=True ,upload_to='documentos/')
    fecha_version =models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.version)