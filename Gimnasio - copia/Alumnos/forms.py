from django.forms import ModelForm
from .models import Plan, Cuota, Alumno
from django.core.exceptions import ValidationError

class planForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

class cuotaForm(ModelForm):
    class Meta:
        model = Cuota
        fields = '__all__'
        labels = {
            'pago': ('Fecha de pago (MM/DD/AAAA)'),
        }

class alumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
