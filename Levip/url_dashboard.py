from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('item/', views.itemPage),
    path('pedido/', views.pedidoPage),
    path('createItemView/', views.createItemView), 
    path('editItemView/<str:item_id>', views.editItemView), 
    path('deleteItem/<str:item_id>', views.deleteItem), 
    path('editItem/', views.editItem, name="editItem"), 
    path('createItem/', views.createItem, name='createItem'), 
]