from django.urls import path
from . import views

urlpatterns = [
    path('listaPlanes', views.listarPlanes, name='listaPlanes'),
    path('crearPlan', views.crearPlan, name='crearPlan'),
    path('editarPlan/<int:id>', views.editarPlan, name='editarPlan'),
    path('borrarPlan/<int:id>', views.borrarPlan, name='borrarPlan'),
    path('listaCuotas', views.listarCuotas, name='listaCuotas'),
    path('crearCuota', views.crearCuota, name='crearCuota'),
    path('listaAlumnos', views.listarAlumnos, name='listaAlumnos'),
    path('crearAlumno', views.crearAlumno, name='crearAlumno'),
    path('editarAlumno/<int:id>', views.editarAlumno, name='editarAlumno'),
    path('borrarAlumno/<int:id>', views.borrarAlumno, name='borrarAlumno')
]