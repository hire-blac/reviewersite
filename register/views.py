from django.shortcuts import redirect, render
from register.forms import Login_Form, RegisterForm
from django.contrib.auth import authenticate, login
from reviewer.decorators import unauthenticated_user

# Create your views here.
@unauthenticated_user
def register(response):
	if response.method == 'POST':
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(response, user)
			print(user)
			return redirect('/')
	else:
		form = RegisterForm()
	return render(response, 'register/register.html',{'title':'Sign up','form':form})

@unauthenticated_user
def user_login(response):
	if response.method == 'POST':
		form = Login_Form(response.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)

			if user is not None:
				login(response, user)
				return redirect('/')
			else:
				context = {
					'title':'No Such User',
					'message':'Invalid login credentials.'
					}
				return render(response, 'main/404.html', context)
	else:
		form = Login_Form()
			
	return render(response, 'registration/login.html', {'title':'User Login', 'form':form})