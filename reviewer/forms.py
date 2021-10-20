from django import forms

class CreateNewReview(forms.Form):
	product = forms.CharField(label='Product', max_length=200)
	rating = forms.IntegerField(label='Rating', min_value=0, max_value=5)
	review = forms.CharField(label='Review', max_length=200)