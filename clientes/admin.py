from email._header_value_parser import Domain

from django.contrib import admin

# Register your models here.
from clientes.models import Clientes, Domicilio

admin.site.register(Clientes)
admin.site.register(Domicilio)
