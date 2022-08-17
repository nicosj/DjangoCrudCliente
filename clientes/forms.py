from django.forms import ModelForm, EmailInput

from clientes.models import Clientes


class ClienteForm(ModelForm):
    class Meta:
        model= Clientes
        fields='__all__'
        widgets={
            'email' : EmailInput(attrs={'type':'email'})
        }