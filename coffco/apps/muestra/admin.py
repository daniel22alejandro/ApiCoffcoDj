from django.contrib import admin
from .models import Muestra

@admin.register(Muestra)
class MuestraAdmin(admin.ModelAdmin):
    list_display = ['cantidad', 'finca', 'usuario', 'codigo', 'fecha']
