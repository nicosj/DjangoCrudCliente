from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from clientes.forms import ClienteForm
from clientes.models import Clientes


def detalleCliente(request,id):
    #cliente = Clientes.objects.get(pk=id)
    cliente = get_object_or_404(Clientes,pk=id)
    return render(request,'clientes/detalle.html', {'cliente':cliente})

def eliminarCliente(request,id):
    cliente = get_object_or_404(Clientes,pk=id)
    if cliente:
        cliente.delete()
    return redirect('index')

#ClienteForm= modelform_factory(Clientes, exclude=[])
def nuevoCliente(request, id=0):
    if request.method == 'POST' and id == 0:
        formCliente= ClienteForm(request.POST)
        if formCliente.is_valid():
            formCliente.save()
            return redirect('index')
    else:
        cliente = get_object_or_404(Clientes, pk=id)
        if request.method == 'POST' and id > 0:
            formCliente = ClienteForm(request.POST, instance=cliente)
            if formCliente.is_valid():
                formCliente.save()
                return redirect('index')
        else:
            if id > 0:
                formCliente=ClienteForm(instance=cliente)

            else:
                formCliente = ClienteForm()

    return render(request, 'clientes/nuevo.html', {'formCliente': formCliente})