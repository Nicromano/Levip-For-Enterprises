
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .User.form import RegisterFormUser

class RegisterUser(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = RegisterFormUser
    success_url = reverse_lazy('dashboard')
