from django.db import models

# Create your models here.

class Entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        ordering = ['apellido']


    
    
    
    
    