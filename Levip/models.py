from django.db import models
# Create your models here.

class Cliente(models.Model):
    CLIE_CEDULA = models.CharField(max_length = 10, primary_key=True), 
    CLIE_USERNAME = models.CharField(max_length= 50, default=None), 
    CLIE_NOMBRE = models.CharField(max_length=50), 
    CLIE_APELLIDO = models.CharField(max_length=50), 
    CLIE_EMAIL = models.CharField(max_length=50), 
    CLIE_PASSWORD = models.TextField(default=None)

class Item(models.Model):
    IT_ID = models.CharField(max_length = 5, primary_key=True)
    IT_DESCRIPCION =  models.TextField(default=None), 
    IT_PRECIO = models.DecimalField(max_digits=10, decimal_places=2)

class Pedido(models.Model):
    PED_ID = models.CharField(max_length = 5, primary_key=True)
    PED_CANTIDAD = models.IntegerField()
    CLIE_CEDULA = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    PED_IT = models.ManyToManyField(Item)
