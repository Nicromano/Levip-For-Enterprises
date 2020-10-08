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
    path('createOrden/', views.createOrden, name='createOrden'),
    path('createOrdenView/', views.createOrdenView), 
    path('editOrderView/<str:order_id>', views.editOrderView), 
    path('editOrder/', views.editOrder, name="editOrder"), 
    path('deleteOrder/<str:order_id>', views.deleteOrder), 
    


]