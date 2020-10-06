from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterFormUser(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]
        labels = {
            'username': 'Username', 
            'first_name': 'Firts name', 
            'last_name':'Last name', 
            'email': 'Email', 
        }