from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view):
	def wrapper_func(response, *args, **kwargs):
		if response.user.is_authenticated:
			return redirect('index')
		else:
			return view(response, *args, **kwargs)
	return wrapper_func