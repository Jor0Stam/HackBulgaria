from django.forms import ModelForm
from django import forms

from Hack_Fmi.user.models import User


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email',
                  'password']
        widgets = {'password': forms.PasswordInput(),
                   'email': forms.EmailInput()}


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email',
                  'password']
        widgets = {'password': forms.PasswordInput(),
                   'email': forms.EmailInput()}
