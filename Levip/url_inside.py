from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('administrator/', views.administrator), 
    path('customer/', views.customer), 
    path('dispached/', views.dispached), 
    path('item/', views.item), 
    path('order_ped/', views.order_ped), 
    path('order/', views.order), 
    path('price/', views.price), 
]