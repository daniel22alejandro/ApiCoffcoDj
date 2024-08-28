from django.db import models
class Tipo_Documento(models.Model):
    nombreDocumento=models.CharField(max_length=150)
    ESTADO_CHOICES=[
        ('activo','activo'),
        ('inactivo','inactivo')
    ]
    estado= models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return self.nombreDocumento