from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Korisnici

class KorisniciRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[(role.value, role.name) for role in Korisnici.RoleChoices])
    status = forms.ChoiceField(choices=[(status.value, status.name) for status in Korisnici.StatusChoices])

    class Meta(UserCreationForm.Meta):
        model = Korisnici
        fields = ('username', 'password1', 'password2', 'role', 'status')