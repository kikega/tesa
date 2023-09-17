from django.contrib import admin

# Register your models here.
from .models import *


class AutomatismoAdmin(admin.ModelAdmin):
    """Lista el estado de los procesos"""
    list_display = ('nombre', 'fecha_creacion', 'fecha_piloto', 'fecha_produccion', 'estado')
    list_filter = ('nombre',)

class TareaAdmin(admin.ModelAdmin):
    """Lista las tareas de un proceso"""
    list_display = ('nombre',)

admin.site.site_header = 'Panel de control RPA'
admin.site.index_title = 'Administración KIKE RPA'
admin.site.site_title = 'Admin RPA'

admin.site.register(Automatismo, AutomatismoAdmin)
admin.site.register(Tarea, TareaAdmin)