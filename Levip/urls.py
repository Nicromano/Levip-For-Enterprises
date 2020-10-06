from django.urls import path, include
from . import views
from .view_class import RegisterUser

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about),
    path('signin/', views.signin),
    path('signup/', RegisterUser.as_view()), 
    path('login/',views.loginPage, name="login"), 
    path('dashboard/', views.dashboard, name="dashboard"), 
    path('logout/', views.logoutPage)
]