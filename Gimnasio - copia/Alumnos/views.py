from django.shortcuts import render, redirect
from .models import Plan, Cuota, Alumno
from .forms import planForm, cuotaForm, alumnoForm

# Create your views here.

def listarPlanes(request):
    planes = Plan.objects.all()
    contexto = {
        'titulo': 'Lista de Planes',
        'planes': planes
    }
    return render(request, 'Alumnos/listaPlanes.html', contexto)

def crearPlan(request):
    formulario = planForm()
    contexto = {
        'form': formulario,
        'mensaje': 'Agregar Plan'
    }
    if request.method == 'POST':
        formularioPOST = planForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('listaPlanes')
        else:
            contexto['mensaje'] += ' - Error en el formulario'
            contexto['form'] = formularioPOST
            return render(request, 'Alumnos/formPlan.html', contexto)
    else:
        return render(request, 'Alumnos/formPlan.html', contexto)

def editarPlan(request, id):
    planEditar = Plan.objects.get(pk=id)
    formEditar = planForm(instance=planEditar)
    contextoGet = {
        'form': formEditar,
        'mensaje': 'Editar Plan'
    }
    if request.method == 'GET':
        return render(request, 'Alumnos/formPlan.html', contextoGet)

    else:
        formGuardar = planForm(request.POST, instance=planEditar)
        if formGuardar.is_valid():
            formGuardar.save()
            return redirect('listaPlanes')

def borrarPlan(request, id):
    planBorrar = Plan.objects.get(pk=id)
    planBorrar.delete()
    return redirect('listaPlanes')

def listarCuotas(request):
    cuotas = Cuota.objects.all()
    contexto = {
        'titulo': 'Lista de Pagos',
        'cuotas': cuotas
    }
    return render(request, 'Alumnos/listaCuotas.html', contexto)

def crearCuota(request):
    formulario = cuotaForm()
    contexto = {
        'form': formulario,
        'mensaje': 'Agregar Pago'
    }
    if request.method == 'POST':
        formularioPOST = cuotaForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('listaCuotas')
        else:
            contexto['mensaje'] += ' - Error en el formulario'
            contexto['form'] = formularioPOST
            return render(request, 'Alumnos/formCuota.html', contexto)
    else:
        return render(request, 'Alumnos/formCuota.html', contexto)

def listarAlumnos(request):
    alumnos = Alumno.objects.all()
    contexto = {
        'titulo': 'Lista de Alumnos',
        'alumnos': alumnos
    }
    return render(request, 'Alumnos/listaAlumnos.html', contexto)

def crearAlumno(request):
    formulario = alumnoForm()
    contexto = {
        'form': formulario,
        'mensaje': 'Nuevo Alumno'
    }
    if request.method == 'POST':
        formularioPOST = alumnoForm(request.POST)
        if formularioPOST.is_valid():
            formularioPOST.save()
            return redirect('listaAlumnos')
        else:
            contexto['mensaje'] += ' - Error en el formulario'
            contexto['form'] = formularioPOST
            return render(request, 'Alumnos/formAlumno.html', contexto)
    else:
        return render(request, 'Alumnos/formAlumno.html', contexto)

def editarAlumno(request, id):
    alumnoEditar = Alumno.objects.get(pk=id)
    formEditar = alumnoForm(instance=alumnoEditar)
    contextoGet = {
        'form': formEditar,
        'mensaje': 'Editar información de Alumno'
    }
    if request.method == 'GET':
        return render(request, 'Alumnos/formAlumno.html', contextoGet)

    else:
        formGuardar = alumnoForm(request.POST, instance=alumnoEditar)
        if formGuardar.is_valid():
            formGuardar.save()
            return redirect('listaAlumnos')

def borrarAlumno(request, id):
    alumnoBorrar = Alumno.objects.get(pk=id)
    alumnoBorrar.delete()
    return redirect('listaAlumnos')