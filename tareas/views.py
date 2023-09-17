from django.shortcuts import render, redirect

# Autenticacion
from django.contrib.auth.decorators import login_required
# Create your views here.

# Importamos los formularios
from .forms import TareaForm

# Importamos los modelos
from tareas.models import Tarea


@login_required
def index(request):
    """Pagina principal de la aplicación"""
    tarea = Tarea.objects.filter(activa=True)
    # context = {
    #     'fecha': tarea['fecha_inicio'],
    #     'tarea': tarea['tarea']
    # }
    return render(request, 'tareas/index.html', {'tarea': tarea})


@login_required
def addTarea(request):
    """Crear nueva tarea"""
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TareaForm()

    return render(request, 'tareas/addtarea.html', {'form': form})
