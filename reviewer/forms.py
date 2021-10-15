from django import forms

class CreateNewReview(forms.Form):
	product = forms.CharField(label="Product",
				max_length=200)

	stars = forms.IntegerField(label="Stars", 
				min_value=1, max_value=5)
	
	review = forms.CharField(label="Review", max_length=200, required=False)