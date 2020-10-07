from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('item/', views.itemPage),
    path('pedido/', views.pedidoPage),
    path('createItemView/', views.createItemView), 
    path('editItemView/<int:link_id>', views.editItemView), 
    path('editItem/', views.editItem), 
    path('createItem/', views.createItem, name='createItem'), 
]