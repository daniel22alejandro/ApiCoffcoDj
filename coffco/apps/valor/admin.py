from django.contrib import admin
from .models import Valor

@admin.register(Valor)
class ValorAdmin(admin.ModelAdmin):
    list_display = ['fk_id_servicio', 'fk_id_detalle', 'valor']
