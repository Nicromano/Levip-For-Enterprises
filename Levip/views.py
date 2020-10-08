from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Cliente, Pedido, Item
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

def itemPage(request):
    try:
        request.session['user']
        return render(request, 'item.html', {'user': Cliente.objects.get(pk=request.session['user']), 'items': Item.objects.all()})
    except:
        return redirect('/levip/signin')

def createItemView(request):
    try:
        request.session['user']
        return render(request, 'formItem.html', {'user': Cliente.objects.get(pk=request.session['user'])} )
    except:
        return redirect('/levip/signin')

def createItem(request):
    try:
        id = request.POST['ID'][0:5]
        price = float(request.POST['precio'])
        descripcion = request.POST['descripcion']
        name = request.POST['name']
        item = Item(IT_ID = id, IT_NOMBRE = name,  IT_PRECIO = price, IT_DESCRIPCION = descripcion)
        item.save()
        return redirect('/levip/dashboard/item')
    except:
        return redirect('/levip/dashboard/createItemView')

def editItemView(request, item_id):
    try:
        request.session['user']
        request.session['item'] = item_id
        return render(request, 'formEditItem.html', {'user': Cliente.objects.get(pk=request.session['user']), 'item': Item.objects.get(pk=item_id)})
    except:
        return redirect('/levip/signin')

def deleteItem(request, item_id):
    try:
        request.session['user']
    except:
        return redirect('/levip/signin')

    try:
        i = Item.objects.get(pk=item_id)
        i.delete()
        return redirect('/levip/dashboard/item')
    except:
        pass

def editItem(request):
    try:
        request.session['user']
    except:
        return redirect('/levip/signin')
    try:
        item = request.session['item']
        del request.session['item']
        i = Item.objects.get(pk=item)
        i.IT_ID = request.POST['ID'][0:5]
        i.IT_NAME = request.POST['name']
        i.IT_PRECIO = float(request.POST['precio'])
        i.IT_DESCRIPCION = request.POST['descripcion']
        i.save()
    except: 
        pass
    return redirect('/levip/dashboard/item')



def createOrden(request):
    try: 
        request.session['user']
    except:
        return redirect('/levip/signin')
    id = request.POST['ID']
    cantidad = request.POST['cantidad']
    item= Item.objects.get(pk=request.POST['item'])
    user = Cliente.objects.get(pk=request.session['user'])
    p = Pedido(PED_ID = id, PED_CANTIDAD = cantidad, CLIE_CEDULA = user, IT_ID = item)
    p.save()
    return redirect('/levip/dashboard/pedido')

def createOrdenView(request):
    try:
        request.session['user']
    except:
        return redirect('/levip/signin')
    return render(request, 'formOrder.html', {'user': Cliente.objects.get(pk=request.session['user']), 'items': Item.objects.all()})


def editOrder(request): 
    try:
        request.session['user']
    except:
        return redirect('/levip/signin')
    pedido = Pedido.objects.get(pk= request.session['order'])
    del request.session['order']
    pedido.PED_ID = request.POST['ID']
    pedido.PED_CANTIDAD = request.POST['cantidad']
    item = Item.objects.get(pk=request.POST['item'])
    pedido.IT_ID = item
    pedido.save()
    return redirect('/levip/dashboard/pedido')

def editOrderView(request, order_id):  
    try:
        request.session['user']
    except:
        return redirect('/levip/signin')
    request.session['order'] = order_id
    return render(request, 'formEditOrder.html', {'user': Cliente.objects.get(pk=request.session['user']), 'pedido': Pedido.objects.get(pk=order_id), 'items': Item.objects.all()})
    

def deleteOrder(request, order_id):  
    try:
        request.session['user']
    except:
        return redirect('/levip/signin')
    
    o = Pedido.objects.get(pk = order_id)
    o.delete()
    return redirect('/levip/dashboard/pedido')


def pedidoPage(request):  
    try:
        request.session['user']
        print(Pedido.objects.filter(CLIE_CEDULA__CLIE_CEDULA = request.session['user']))
        return render(request, 'order.html', {'user': Cliente.objects.get(pk=request.session['user']), 'orders': Pedido.objects.filter(CLIE_CEDULA__CLIE_CEDULA = request.session['user']), 'items': Item.objects.all()})
    except:
        return redirect('/levip/signin')

