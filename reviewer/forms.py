from django import forms

class CreateNewReview(forms.Form):
	product = forms.CharField(label='Product', max_length=200)
	rating = forms.IntegerField(label='Rating', min_value=0, max_value=5)
	review = forms.CharField(widget=forms.Textarea,label='Review', max_length=200)
	
class findUser(forms.Form):
	username = forms.CharField(empty_value='Search for user')