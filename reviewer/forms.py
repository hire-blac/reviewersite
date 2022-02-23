from django import forms

from reviewer.models import Category

class CreateNewProduct(forms.Form):
    choices = []
    categories = Category.objects.all()
    for category in categories:
        choices.append((category.id, category.name))
    
    choices.append(('other', 'other...'))

    category = forms.ChoiceField(label='Category', widget=forms.Select, choices=choices)
    name = forms.CharField(label='Name', max_length=200)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=200, required=False)
