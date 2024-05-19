# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Agendas

class LoginForm(forms.Form):
    username = forms.CharField(label='Nome de usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    user_type = forms.ChoiceField(choices=[('aluno', 'Aluno'), ('professor', 'Professor')])

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'user_type']
        

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agendas
        fields = ['professor', 'local', 'data', 'hora', 'status']
