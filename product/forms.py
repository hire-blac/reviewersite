from dataclasses import fields
from django import forms
from django.forms import ModelForm
from . models import *

from eav.forms import BaseDynamicEntityForm

class ProductAdminForm(BaseDynamicEntityForm):
    model = Product

    def __init__(self, *args, **kwargs):
        super(ProductAdminForm, self).__init__(*args, **kwargs)
        fields = self.fields

        # fields['category'].widget.attrs = {'class': 'car', 'default':'Category'}
        fields['name'].widget.attrs = {'class': 'car music book others', 'placeholder':'Name/Title'}
        fields['model'].widget.attrs = {'class': 'car', 'placeholder':'Model'}
        fields['make'].widget.attrs = {'class': 'car', 'placeholder':'Make'}
        fields['artist'].widget.attrs = {'class': 'music', 'placeholder':'Artist name'}
        fields['album'].widget.attrs = {'class': 'music', 'placeholder':'Album name'}
        fields['featuring'].widget.attrs = {'class': 'music', 'placeholder':'Featuring'}
        fields['genre'].widget.attrs = {'class': 'music book', 'placeholder':'Genre'}
        fields['author'].widget.attrs = {'class': 'book', 'placeholder':'Author name'}
        fields['isbn'].widget.attrs = {'class': 'book', 'placeholder':'Book ISBN'}
        fields['year'].widget.attrs = {'class': 'car music book', 'placeholder':'Year released'}
        fields['category-name'].widget.attrs = {'class': 'others', 'placeholder':'Category name'}

    class Meta:
        model = Product
        fields = '__all__'

class NewProductForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'