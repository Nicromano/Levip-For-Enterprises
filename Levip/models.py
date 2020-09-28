from django.db import models

# Create your models here.


class Cliente(models.Model):
    CLIE_CEDULA = models.CharField(max_length = 10, primary_key=True)
    CLIE_NOMBRE = models.CharField(max_length=50)
    CLIE_RUC = models.CharField(max_length=13, blank=True)


class Direccion(models.Model):
    DIR_CODIGO = models.CharField(max_length=5, primary_key=True)
    DIR_TIPO = models.CharField(max_length=100)
    CLIE_CEDULA = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Despachador(models.Model):
    DES_ID = models.CharField(max_length = 5, primary_key=True)
    DES_NOMBRE = models.CharField(max_length = 25)
    DES_APELLIDO = models.CharField(max_length = 25)
    DES_TELEFONO = models.CharField(max_length = 10, blank = True)
    
class Orden(models.Model):
    ORD_ID = models.CharField(max_length = 5, primary_key=True)
    ORD_ENCABEZADO = models.TextField()
    DES_ID = models.ForeignKey(Despachador,on_delete=models.CASCADE )

class Precio(models.Model):
    PRE_ID = models.CharField(max_length = 5, primary_key=True)
    PRE_FECHA_INICIO = models.DateField()
    PRE_FECHA_FINAL = models.DateField()


class Item(models.Model):
    IT_ID = models.CharField(max_length = 5, primary_key=True)
    IT_MEDIDA = models.DecimalField(decimal_places=2)
    IT_DESCRIPCION = models.TextField()
    DES_ID = models.ForeignKey(Despachador, on_delete=models.CASCADE)
    ORD_ID = models.ForeignKey(Orden, on_delete=models.CASCADE)
    PRE_ID = models.ForeignKey(Precio, on_delete=models.CASCADE)

class Pedido(models.Model):
    PED_ID = models.CharField(max_length = 5, primary_key=True)
    PED_CANTIDAD = models.IntegerField()
    CLIE_CEDULA = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    IT_ID = models.ManyToManyField(Item)

    
class Administrador(models.Model):
    ADMIN_ID = models.CharField(max_length = 5, primary_key=True)
    ADMIN_USUARIO = models.CharField(max_length=50)
    ADMIN_CONTRASENA = models.TextField()
    CLIE_CEDULA = models.ManyToManyField(Cliente)
    IT_CODIGO = models.ManyToManyField(Item)
