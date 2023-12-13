from django.db import models
from Actividades.models import Actividad
# Create your models here.

class Plan(models.Model):
    nombre = models.CharField(max_length=20)
    importe = models.FloatField()

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['importe']

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.PositiveIntegerField()
    dni = models.PositiveIntegerField()
    email = models.EmailField()
    plan = models.ForeignKey(Plan, null=True, blank=True, on_delete=models.DO_NOTHING, db_constraint=False)
    actividades = models.ManyToManyField(Actividad, null=True, blank=True)

    def __str__(self):
        return self.apellido

    class Meta:
        ordering = ['apellido']

class Cuota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING, db_constraint=False)
    emision = models.DateField(auto_now_add=True)
    pago = models.DateField(null=True, blank=True)
    

