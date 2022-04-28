from django import forms
from django.forms import ModelForm
from . models import *

class NewProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['slug', 'category']