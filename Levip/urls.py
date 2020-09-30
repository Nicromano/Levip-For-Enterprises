from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about),
    path('signin/', views.signin),
    path('login/',views.loginPage, name="login"), 
    path('dashboard/', views.dashboard), 
    path('logout/', views.logoutPage)
]