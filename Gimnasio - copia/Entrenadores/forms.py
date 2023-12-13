from django.forms import ModelForm
from .models import Entrenador

class entrenadorForm(ModelForm):
    class Meta:
        model = Entrenador
        fields = '__all__'


