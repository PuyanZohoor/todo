
from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
