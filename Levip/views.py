from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Direccion, Cliente, Pedido, Administrador, Precio, Despachador, Orden, Pedido
# Create your views here.
#
# Rutas que no necesitan protección de rutas
#
def index(request):
    if request.user.username:
        return redirect('/levip/dashboard') 
    return render(request, 'home.html')

def about(request):
    if request.user.username:
        return redirect('/levip/dashboard') 
    return render(request, 'about.html')

def signin(request):
    if request.user.username:
        return redirect('/levip/dashboard') 
    return render(request, 'signin.html')

def loginPage(request):
    if request.user.username:
        return redirect('/levip/dashboard') 
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/levip/dashboard') 
    else:
        return redirect('/levip/signin')

#
# Rutas que necesitan protección de rutas
#
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('/levip/signin')

@login_required
def administrator(request):
    return render(request, 'Objects/administrator.html', {'admins': Administrador.objects.all() })

@login_required
def customer(request):
    return render(request, 'Objects/customer.html', {'customers': Cliente.objects.all(), 'dirs': Direccion.objects.all() })

@login_required
def dispached(request):
    return render(request, 'Objects/dispached.html', {'dispacheds': Despachador.objects.all()})

@login_required
def item(request):
    return render(request, 'Objects/item.html', {'items': Item.objects.all(), 'despachador': Despachador.objects.all(), 'prices': Precio.objects.all()})

@login_required
def order_ped(request):
    return render(request, 'Objects/order_ped.html', {'pedidos': Pedido.objects.all(), 'customers': Cliente.objects.all()})

@login_required
def order(request):
    return render(request, 'Objects/order.html', {'orders': Orden.objects.all(), 'despachador': Despachador.objects.all()})

@login_required
def price(request):
    return render(request, 'Objects/price.html', {'prices': Precio.objects.all()})
