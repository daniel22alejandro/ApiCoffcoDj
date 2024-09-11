from django.contrib import admin
from .models import Tipo_Documento

@admin.register(Tipo_Documento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ['nombreDocumento', 'estado']
