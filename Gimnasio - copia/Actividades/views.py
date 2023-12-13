from django.shortcuts import render, redirect
from .models import Dia, Horario, Actividad, Clase
from Alumnos.models import Alumno
from .forms import diaForm, horarioForm, actividadForm, claseForm

# Create your views here.

def principal(request):
    return render(request, 'Actividades/HomePage.html')

def listarDias(request):
    dias = Dia.objects.all()
    contexto = {
        'titulo': 'Lista de Dias',
        'dias': dias
    }
    return render(request, 'Actividades/listaDias.html', contexto)

def crearDia(request):
    formulario = diaForm()
    contexto = {
        'form': formulario,
        'mensaje': 'Agregar Día'
    }
    if request.method == 'POST':
        formularioPOST = diaForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('listaDias')
        else:
            contexto['mensaje'] += 'Error en el formulario'
            contexto['form'] = formularioPOST
            return render(request, 'Actividades/formDia.html', contexto)
    else:
        return render(request, 'Actividades/formDia.html', contexto)

def listarHorarios(request):
    horarios = Horario.objects.all()
    contexto = {
        'titulo': 'Lista de Horarios',
        'horarios': horarios
    }
    return render(request, 'Actividades/listaHorarios.html', contexto)

def crearHorario(request):
    formulario = horarioForm()
    contexto = {
        'form': formulario,
        'mensaje': 'Agregar Horario'
    }
    if request.method == 'POST':
        formularioPOST = horarioForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('listaHorarios')
        else:
            contexto['mensaje'] += 'Error en el formulario'
            contexto['form'] = formularioPOST
            return render(request, 'Actividades/formHorario.html', contexto)
    else:
        return render(request, 'Actividades/formHorario.html', contexto)

def listarActividades(request):
    actividades = Actividad.objects.all()
    alumnos = Alumno.objects.all()
    contexto = {
        'titulo': 'Lista de Actividades',
        'actividades': actividades,
        'alumnos': alumnos
    }
    return render(request, 'Actividades/listaActividades.html', contexto)

def crearActividad(request):
    formulario = actividadForm()
    contexto = {
        'form': formulario,
        'mensaje': 'Agregar Actividad'
    }
    if request.method == 'POST':
        formularioPOST = actividadForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('listaActividades')
        else:
            contexto['mensaje'] += 'Error en el formulario'
            contexto['form'] = formularioPOST
            return render(request, 'Actividades/formActividad.html', contexto)
    else:
        return render(request, 'Actividades/formActividad.html', contexto)

def editarActividad(request, id):
    actividadEditar = Actividad.objects.get(pk=id)
    formEditar = actividadForm(instance=actividadEditar)
    contextoGet = {
        'form': formEditar,
        'mensaje': 'Editar Actividad'
    }
    if request.method == 'GET':
        return render(request, 'Actividades/formActividad.html', contextoGet)

    else:
        formGuardar = actividadForm(request.POST, instance=actividadEditar)
        if formGuardar.is_valid():
            formGuardar.save()
            return redirect('listaActividades')

def borrarActividad(request, id):
    actividadBorrar = Actividad.objects.get(pk=id)
    actividadBorrar.delete()
    return redirect('listaActividades')

def listarClases(request):
    clases = Clase.objects.all()
    contexto = {
        'titulo': 'Lista de Clases',
        'clases': clases
    }
    return render(request, 'Actividades/listaClases.html', contexto)

def crearClase(request):
    formulario = claseForm()
    contexto = {
        'form': formulario,
        'mensaje': 'Agregar Clase'
    }
    if request.method == 'POST':
        formularioPOST = claseForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('listaClases')
        else:
            contexto['mensaje'] += 'Error en el formulario'
            contexto['form'] = formularioPOST
            return render(request, 'Actividades/formClase.html', contexto)
    else:
        return render(request, 'Actividades/formClase.html', contexto)