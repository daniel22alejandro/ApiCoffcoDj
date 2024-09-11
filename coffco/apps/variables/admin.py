# apps/variables/admin.py
from django.contrib import admin
from .models import VariblesModel

@admin.register(VariblesModel)
class VariblesModelAdmin(admin.ModelAdmin):
    list_display = ['nombreVaribles', 'estadovarible', 'tipo_Dato']