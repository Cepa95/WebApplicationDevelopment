from django import forms
from .models import Projekcija

class ProjekcijaForm(forms.ModelForm):
    class Meta:
        model = Projekcija
        fields = ['movie', 'time', 'capacity']