from django.db import models
from apps.finca.models import Finca
from django.db.models import SET_NULL
from apps.user.models import User
class Muestra(models.Model):
    cantidad=models.DecimalField(max_digits=10, decimal_places=2)
    finca=models.ForeignKey(Finca,on_delete=SET_NULL,null=True,blank=True )
    usuario = models.ForeignKey(User,on_delete=SET_NULL, null=True, blank=True)
    codigo=models.CharField(max_length=100)
    fecha=models.DateField(auto_now=True)
    def __str__(self):
        return str(self.finca)
        