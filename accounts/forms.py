from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from . models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        
class EditProfileForm(ModelForm):
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user', 'followers']