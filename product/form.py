from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    fullname = forms.CharField(label='Full Name', max_length=500)

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password1', 'password2']
