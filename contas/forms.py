from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['cpf', 'username', 'name', 'email', 'telefone',]


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['cpf', 'username', 'name', 'email', 'telefone', 'is_active', 'is_staff']