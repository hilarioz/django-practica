from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='HomePage'),
    path('listaDias', views.listarDias, name='listaDias'),
    path('crearDia', views.crearDia, name='crearDia'),
    path('listaHorarios', views.listarHorarios, name='listaHorarios'),
    path('crearHorario', views.crearHorario, name='crearHorario'),
    path('listaActividades', views.listarActividades, name='listaActividades'),
    path('crearActividad', views.crearActividad, name='crearActividad'),
    path('editarActividad/<int:id>', views.editarActividad, name='editarActividad'),
    path('borrarActividad/<int:id>', views.borrarActividad, name='borrarActividad'),
    path('listaClases', views.listarClases, name='listaClases'),
    path('crearClase', views.crearClase, name='crearClase')
]