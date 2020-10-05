from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about),
    path('signin/', views.signin),
    path('login/',views.loginPage, name="login"), 
    path('dashboard/', include('Levip.url_inside')), 
    path('logout/', views.logoutPage)
]