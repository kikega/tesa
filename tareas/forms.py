from django import forms

from tareas.models import Tarea


class TareaForm(forms.ModelForm):
    """Formulario Tarea"""

    class Meta:
        model = Tarea
        fields = [
            'tarea',
            'cliente',
            'descripcion',
            'fecha_fin',
        ]
