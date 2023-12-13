from django.urls import path
from . import views

urlpatterns = [
    path('listaEntrenadores', views.listarEntrenadores, name='listaEntrenadores'),
    path('crearEntrenador', views.crearEntrenador, name='crearEntrenador'),
    path('editarEntrenador/<int:id>', views.editarEntrenador, name='editarEntrenador'),
    path('borrarEntrenador/<int:id>', views.borrarEntrenador, name='borrarEntrenador'),
]