from django.db import models
from Entrenadores.models import Entrenador

# Create your models here.

class Dia(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Horario(models.Model):
    horario = models.CharField(max_length=50)

    def __str__(self):
        return self.horario 

class Actividad(models.Model):
    nombre = models.CharField(max_length=50)
    dia = models.ForeignKey(Dia, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    entrenadores = models.ManyToManyField(Entrenador)

    def __str__(self):
        return f'{self.nombre} {self.dia} {self.horario}'

    class Meta:
        ordering = ['id']

class Clase(models.Model):
    fecha = models.DateField(auto_now_add=True)
    actividad = models.ForeignKey(Actividad, on_delete=models.DO_NOTHING)
    asistencia = models.CharField(max_length=30, default='Sin registro')


