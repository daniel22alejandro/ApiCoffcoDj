from django.contrib import admin
from .models import TipoServicio

@admin.register(TipoServicio)
class TipoServicioAdmin(admin.ModelAdmin):
    list_display = ['nombreServicio', 'estado']
