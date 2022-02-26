from django import forms
from django.forms import ModelForm
from . models import *

from eav.forms import BaseDynamicEntityForm

class ProductAdminForm(BaseDynamicEntityForm):
    model = Product

    class Meta:
        model = Product
        fields = '__all__'

