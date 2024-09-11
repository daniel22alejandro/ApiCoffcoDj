from django.contrib import admin
from .models import Documento

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_carga', 'codigo_documento', 'descripcion', 'fecha_Emision', 'fk_tipoServicio', 'fkTipoDocumentos']
