from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from review.forms import NewComment
from review.models import Review
from product.models import Category

# Create your views here.

# homepage
def index(response):
    reviews = Review.objects.all().order_by('-created')
    categories = Category.objects.all()
    user = response.user
    comment_form = NewComment
    context = {
        'title': 'Homepage',
        'reviews':reviews,
        'categories': categories,
        'user': user,
        'comment_form': comment_form
        }

    return render(response, 'main/index.html', context )

# find user
def find_user(response):
    if response.method == "POST":
        form = response.POST
        print(form['username'])
        user = User.objects.get(username=form['username'])
        return HttpResponse(user)
