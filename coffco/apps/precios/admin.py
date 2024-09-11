from django.contrib import admin
from .models import PreciosModels

@admin.register(PreciosModels)
class PreciosModelsAdmin(admin.ModelAdmin):
    list_display = ['presentacion', 'precio', 'tipoServicio', 'servicio', 'estado']
