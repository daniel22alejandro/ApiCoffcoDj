from django.db import models

class VariblesModel(models.Model):
    nombreVaribles=models.CharField(max_length=500)
    ESTADO_CHOICES=[
        ('activo','activo'),
        ('inactivo','inactivo')
    ]
    estadovarible= models.CharField(max_length=20, choices=ESTADO_CHOICES, default='activo')
    TIPO_DATO_CHOICES = [
    ('text', 'Texto'),
    ('number', 'Numero'),
    ('date', 'Fecha'),
    ]

    tipo_Dato=models.CharField(max_length=20, choices=TIPO_DATO_CHOICES)

    def __str__(self):
        return self.nombreVaribles