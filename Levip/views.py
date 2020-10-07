from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Cliente, Pedido
# Create your views here.
#
# Rutas que no necesitan protección de rutas
#
def index(request):
    try:  # Excepción por si no existe un usuario registrado
        request.session['user'] 
        return redirect('/levip/dashboard')   # Redirigue a la página /dashboard
    except:
        # Renderia el archivo login.html existente en templates/polls
        return render(request, 'home.html')

def about(request):

    try:  # Excepción por si no existe un usuario registrado
        request.session['user'] 
        return redirect('/levip/dashboard')   # Redirigue a la página /dashboard
    except:
        # Renderia el archivo about.html existente en templates/polls
        return render(request, 'about.html')

def signin(request):
    try:  # Excepción por si no existe un usuario registrado
        request.session['user'] 
        return redirect('/levip/dashboard')   # Redirigue a la página /dashboard
    except:
        # Renderia el archivo singin.html existente en templates/polls
        return render(request, 'signin.html')

def signup(request):
    try:  # Excepción por si no existe un usuario registrado
        request.session['user'] 
        return redirect('/levip/dashboard')   # Redirigue a la página /dashboard
    except:
        # Renderia el archivo signup.html existente en templates/polls
        return render(request, 'signup.html')

def signupPage(request):
    CI = str(request.POST['CI'])
    username = request.POST['username']
    firts_name = request.POST['firts_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password1:
        #registra
        user = Cliente(
            CLIE_CEDULA = CI, CLIE_USERNAME = username, CLIE_NOMBRE = firts_name, CLIE_APELLIDO = last_name, CLIE_EMAIL = email, CLIE_PASSWORD = password1
        )
        user.save()
        request.session['user'] = user.CLIE_CEDULA
        return redirect('/levip/dashboard')
    else:
        return redirect('/levip/signup')

def loginPage(request):
    username = request.POST['username']
    password = request.POST['password']
    id = Cliente.objects.filter(
        CLIE_USERNAME__iexact = username, CLIE_PASSWORD = password
    ).values_list('CLIE_CEDULA', flat=True)
    if len(id) == 0:
        # No existe 
        return redirect('/levip/signin')
    else:
        request.session['user'] = id[0]
        return redirect('/levip/dashboard')

def dashboard(request):
    try:
        request.session['user']
        return render(request, 'dashboard.html', {'user': Cliente.objects.get(pk=request.session['user'])})
    except:
        return redirect('/levip/signin')

def logoutPage(request):
    del request.session['user']
    return redirect('/levip/signin')
