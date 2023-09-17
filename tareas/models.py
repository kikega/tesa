"""
Modelos para la gestión de las tareas
"""
from django.db import models
# Importamos los modelos de Cliente
#from clientes.models import Cliente, Central, Modulo
# Create your models here.


class Tarea(models.Model):
    """Tareas a realizar"""
    tarea = models.CharField('Titulo de la tarea', max_length=50)
    cliente = models.ForeignKey('clientes.Cliente', verbose_name=(
        "Clientes"), on_delete=models.CASCADE, null=True)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField(
        'Fecha de creación', auto_now=True)
    fecha_fin = models.DateTimeField(
        'Fecha finalización', auto_now=False, auto_now_add=False, blank=True, null=True)
    activa = models.BooleanField(default=True)

    class Meta:
        """Ordena los resultados por fecha de inicio"""
        ordering = ['fecha_inicio']

    def __str__(self):
        return '{} - {}'.format(self.tarea, self.fecha_inicio)
