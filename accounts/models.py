from django.db import models
from core.models import Funcionario
from django import forms

class FormFuncionario(forms.ModelForm):
    class Meta:
        model = Funcionario
        exclude = ()
