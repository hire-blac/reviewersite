from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class Login_Form(forms.Form):
	username = forms.CharField(label='Username', required=True )
	password = forms.CharField(widget=forms.PasswordInput,label='Password', required=True )