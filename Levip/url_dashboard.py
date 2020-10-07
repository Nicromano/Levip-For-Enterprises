from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('item/', views.itemPage),
    path('pedido/', views.pedidoPage),
]