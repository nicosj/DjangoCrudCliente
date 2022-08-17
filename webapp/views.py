from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from clientes.models import Clientes


def bienvenido(request):
    no_personas = Clientes.objects.count()
    #client = Clientes.objects.all()
    client = Clientes.objects.order_by('id')
    return render(request, 'bienvenido.html', {'no_personas':no_personas, 'client': client, })
