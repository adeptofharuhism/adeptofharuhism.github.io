from django import forms
from .models import NewUser, AuthUser

class AuthForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ('username', 'password')

class NUForm(forms.ModelForm):
    class Meta:
        model = NewUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name')