from django.db import models

# Create your models here.

class usuario(models.Model):

    nombre= models.CharField(max_length=200, verbose_name="Nombre")
    id_user = models.CharField(max_length=200, verbose_name="ID")
    cel = models.CharField(max_length=200, verbose_name="Telefono")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-created"]
    def __str__(self):
        return self.nombre