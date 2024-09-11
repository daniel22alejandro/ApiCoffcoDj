from django.db import models
from apps.logos.models import Logo
from apps.documentos.models import Documento

class LogoDocumento(models.Model):
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE)
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE)

    def __str__(self):
        return self.logo



# f"Logo: {self.logo.nombre} - Documento: {self.documento.nombre}"