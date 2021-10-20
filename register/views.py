from django.shortcuts import redirect, render
from register.forms import RegisterForm

# Create your views here.
def register(response):
	if response.method == 'POST':
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = RegisterForm()
	return render(response, 'register/register.html',{'title':'Sign up','form':form})