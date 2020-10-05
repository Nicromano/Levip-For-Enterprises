from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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
