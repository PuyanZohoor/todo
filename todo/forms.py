
from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.CharField()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()