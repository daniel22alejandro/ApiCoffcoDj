from django.db import models

class TipoServicio(models.Model):
    nombreServicio=models.CharField(max_length=200)
    ESTADO_CHOICES=[
        ('activo','activo'),
        ('inactivo','inactivo')
    ]
    estado= models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')
