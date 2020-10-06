from django.db import models

# Create your models here.

class Cliente(models.Model):
    CLIE_CEDULA = models.CharField(max_length = 10, primary_key=True)
    CLIE_NOMBRE = models.CharField(max_length=50)
    CLIE_RUC = models.CharField(max_length=13, blank=True)

class Pedido(models.Model):
    PED_ID = models.CharField(max_length = 5, primary_key=True)
    PED_CANTIDAD = models.IntegerField()
    CLIE_CEDULA = models.ForeignKey(Cliente, on_delete=models.CASCADE)


    