from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'tipo_servicio', 'fecha', 'ambiente', 'muestra', 'usuario', 'estado', 'fecha_inicio', 'fecha_fin']
