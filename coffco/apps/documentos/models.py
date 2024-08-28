
from django.db import models
from apps.tipo_servicios.models import TipoServicio
from apps.tipo_documento.models import Tipo_Documento
from django.db.models import SET_NULL


class Documento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_carga = models.DateField(null=True)
    descripcion = models.TextField(blank=True, null=True)
    codigo_documentos = models.CharField(max_length=100, null=True, blank=True)

    descripcion= models.CharField(max_length=200)
    fecha_Emision= models.DateField(null=True)
    fk_tipoServicio=models.ForeignKey(TipoServicio,on_delete=SET_NULL, null=True, blank=True)
    fkTipoDocumentos=models.ForeignKey(Tipo_Documento,on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre