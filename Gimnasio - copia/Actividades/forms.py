from django.forms import ModelForm
from .models import Dia, Horario, Actividad, Clase

class diaForm(ModelForm):
    class Meta:
        model = Dia
        fields = '__all__'

class horarioForm(ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'

class actividadForm(ModelForm):
    class Meta:
        model = Actividad
        fields = '__all__'

class claseForm(ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'