# apps/logos/models.py
from django.db import models

class Logo(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    ]
    
    ruta = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')
    nombre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre 
