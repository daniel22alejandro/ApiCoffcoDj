from django.db import models

class Municipio(models.Model):
    nombre_municipio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_municipio
    
