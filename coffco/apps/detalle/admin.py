from django.contrib import admin
from .models import Detalle

@admin.register(Detalle)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ['versiones', 'variables']







# from django.contrib import admin
# from apps.detalle.models import Detalle


# admin.site.register(Detalle)

