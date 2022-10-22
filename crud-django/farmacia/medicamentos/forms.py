from django import forms
from django import forms
from medicamentos.models import Remedio

class FormRemedio(forms.ModelForm):
    class Meta:
        model= Remedio
        fields = '__all__'