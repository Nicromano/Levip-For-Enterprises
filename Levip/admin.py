from django.contrib import admin

# Register your models here.
from .models import Cliente, Administrador, Item, Despachador, Precio, Orden, Direccion, Pedido

admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Item)
admin.site.register(Despachador)
admin.site.register(Precio)
admin.site.register(Orden)
admin.site.register(Direccion)
admin.site.register(Pedido)