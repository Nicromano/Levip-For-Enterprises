from django.contrib import admin

# Register your models here.
from .models import Cliente, Pedido

admin.site.register(Cliente)
admin.site.register(Pedido)