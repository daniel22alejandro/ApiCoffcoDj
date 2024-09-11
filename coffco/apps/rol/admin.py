from django.contrib import admin
from .models import RolModels

@admin.register(RolModels)
class RolModelsAdmin(admin.ModelAdmin):
    list_display = ['rol']

