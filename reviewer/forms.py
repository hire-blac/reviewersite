from django import forms
from django.forms.widgets import Textarea

from reviewer.models import Category

class CreateNewReview(forms.Form):
	rating = forms.IntegerField(label='Rating', min_value=0, max_value=5)
	review = forms.CharField(widget=forms.Textarea,label='Review', max_length=200)
	
class CreateNewProduct(forms.Form):
	choices = []
	categories = Category.objects.all()
	for category in categories:
		choices.append((category.id, category.name))
	
	category = forms.ChoiceField(label='Category', widget=forms.Select, choices=choices)
	name = forms.CharField(label='Name', max_length=200)
	description = forms.CharField(label='Description', widget=forms.Textarea, max_length=200, required=False)