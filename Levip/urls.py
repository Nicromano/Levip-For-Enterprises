from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about),
    path('signin/', views.signin),
    path('signup/', views.signup), 
    path('login/',views.loginPage, name="login"), 
    path('register/',views.signupPage, name="register"), 
    path('dashboard/', include('Levip.url_dashboard')), 
    path('logout/', views.logoutPage), 
]