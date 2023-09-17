"""Modelos para los clientes"""
from django.db import models

# Create your models here.


class Cliente(models.Model):
    """Clase cliente"""
    nombre = models.CharField('Nombre del cliente', max_length=50)
    coordinador = models.CharField('Coordinador', max_length=50)
    telefCoord = models.CharField('Telefono coordinador', max_length=9)
    correoCoord = models.EmailField('Correo coordinador', max_length=254)

    def __str__(self):
        return str(self.nombre)

    class Meta:
        """Ordena los resultados por nombre"""
        ordering = ['nombre']
