from django.db import models
from usuarios.models import usuario

# Create your models here.

class transaccion(models.Model):
    
    user =models.ForeignKey(usuario, null= True, blank= True, on_delete=models.CASCADE)
    dinero= models.CharField(max_length=200, null=False, verbose_name="Dinero")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"
        ordering = ["-created"]
    def __str__(self):
        return self.user