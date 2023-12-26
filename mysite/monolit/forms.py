from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'avatar', 'info', 'password1', 'password2')
