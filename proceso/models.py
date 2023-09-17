"""Modelos de la Base de Datos"""
from django.db import models

# Create your models here.
class Automatismo(models.Model):
    """Tabla que gestiona la parte fundamental de un proceso"""
    nombre = models.CharField('Nombre', max_length=75, blank=False, null=False)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now=True)
    fecha_piloto = models.DateTimeField('Fecha Piloto', auto_now=False, auto_now_add=False, blank=True, null=True)
    fecha_produccion = models.DateTimeField('Fecha Produccion', auto_now=False, auto_now_add=False, blank=True, null=True)
    ESTADO = (
        ('des', 'Desarrollo'),
        ('pil', 'Piloto'),
        ('pro', 'Produccion'),
    )
    estado = models.CharField('Estado', max_length=3, choices=ESTADO)
    observaciones = models.TextField('Observaciones',blank=True, null=True)

    class Meta:
        """Ordena los resultados por fecha de inicio"""
        ordering = ['fecha_creacion']
        verbose_name_plural = "Automatismos"

    def __str__(self):
        return f'{self.nombre}.  {self.fecha_creacion}'


class Tarea(models.Model):
    """Tareas de las que se compone un proceso"""
    nombre = models.CharField('Nombre', max_length=75, blank=False, null=False)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    id_automatismo = models.ForeignKey(Automatismo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Tareas"

    def __str__(self):
        return f'{self.nombre}'


class Sistema(models.Model):
    """Sistemas con los que interactúa un proceso"""
    nombre = models.CharField('Nombre', max_length=75, blank=False, null=False)
    usuario = models.CharField('Usuario', max_length=15, blank=True, null=True)
    password = models.CharField('Password', max_length=15, blank=True, null=True)
    aplicacion = models.CharField('Aplicación', max_length=15, blank=True, null=True)
    rol = models.CharField('Rol', max_length=15, blank=True, null=True)
    observaciones = models.TextField('Observaciones',blank=True, null=True)
    id_automatismo = models.ForeignKey(Automatismo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sistemas"

    def __str__(self):
        return f'{self.nombre}'


class Diagrama(models.Model):
    """Diagrams de la solución"""
    TIPO = (
        ('g', 'general'),
        ('e', 'etapa'),
    )
    nombre = models.CharField('Nombre', max_length=75, blank=False, null=False)
    tipo = models.CharField('Tipo', max_length=1, choices=TIPO)
    diagrama = models.ImageField(upload_to='diagramas', blank=True, null=True)
    observaciones = models.TextField('Observaciones',blank=True, null=True)
    id_automatismo = models.ForeignKey(Automatismo, on_delete=models.CASCADE)

    class Meta:
        """Devuelve el plural de la clase"""
        verbose_name_plural = "Diagramas"

    def __str__(self):
        return self.nombre


class Hito(models.Model):
    """Documentación que se ha de hacer durante el desarrollo del proceso"""
    pdd = models.BooleanField('PDD', default=False)
    pdd_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    sdd = models.BooleanField('SDD', default=False)
    sdd_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    pipma = models.BooleanField('PIPMA', default=False)
    pipma_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    ttd = models.BooleanField('TTD', default=False)
    ttd_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    trnd = models.BooleanField('TRND', default=False)
    trnd_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    tdmut = models.BooleanField('TDMUT', default=False)
    tdmut_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    qa = models.BooleanField('QA', default=False)
    qa_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    miti = models.BooleanField('MITI', default=False)
    miti_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    crq_piloto = models.BooleanField('CRQ Piloto', default=False)
    crq_piloto_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    crq_produccion = models.BooleanField('CRQ Producción', default=False)
    crq_produccion_fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    observaciones = models.TextField('Observaciones',blank=True, null=True)
    id_automatismo = models.ForeignKey(Automatismo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Hitos"


class Objeto(models.Model):
    """Objeto crerado en el espionaje o interacción de una aplicación"""
    nombre = models.CharField('Nombre', max_length=75, blank=False, null=False)
    xml = models.TextField('XML', blank=True, null=True)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    id_automatismo = models.ForeignKey(Automatismo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Objetos"

    def __str__(self):
        return self.nombre


class Pagina(models.Model):
    """Datos relevantes de una página de un proceso"""
    nombre = models.CharField('Nombre', max_length=75, blank=False, null=False)
    xml = models.TextField('XML', blank=True, null=True)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    id_automatismo = models.ForeignKey(Automatismo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.nombre


class Parametro(models.Model):
    """Parámetro de una página"""
    TIPO = (
        ('i', 'input'),
        ('o', 'output'),
        ('e', 'exception')
        )

    tipo = models.CharField('Tipo', max_length=1, choices=TIPO)
    nombre = models.CharField('Nombre', max_length=75, blank=False, null=False)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    tipo_variable = models.CharField('Tipo variable', max_length=15, blank=True, null=True)
    valor = models.CharField(max_length=60, blank=True, null=True)
    id_parametro = models.ForeignKey(Pagina, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Parámetros"

    def __str__(self):
        return self.nombre

class Problema(models.Model):
    """Datos relevantes de una página de un proceso"""
    nombre = models.CharField('Nombre', max_length=200, blank=False, null=False)
    descripcion = models.TextField('Descripción', blank=True, null=True)
    resuelto = models.BooleanField('Resuelto', default=False, blank=True, null=True)
    id_automatismo = models.ForeignKey(Automatismo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Problemas"

    def __str__(self):
        return self.nombre
