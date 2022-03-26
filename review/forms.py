from django import forms

class CreateNewReview(forms.Form):
	rating = forms.IntegerField(label='Rating', min_value=0, max_value=5)
	review = forms.CharField(widget=forms.Textarea,label='Review')

class NewComment(forms.Form):
	comment = forms.CharField(widget=forms.Textarea, initial='Write a comment...')

class NewReply(forms.Form):
	reply = forms.CharField(widget=forms.Textarea, initial='reply to this comment...')

