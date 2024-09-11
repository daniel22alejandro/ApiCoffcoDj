from django.contrib import admin
from .models import Versione

@admin.register(Versione)
class VersioneAdmin(admin.ModelAdmin):
    list_display = ['version', 'documento', 'estado', 'nombre_documento', 'fecha_version']
