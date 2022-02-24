from django import forms

class CreateNewReview(forms.Form):
	rating = forms.IntegerField(label='Rating', min_value=0, max_value=5)
	review = forms.CharField(widget=forms.Textarea,label='Review')
