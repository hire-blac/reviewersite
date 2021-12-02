from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from reviewer.forms import CreateNewReview
from .models import Profile, Review

# Create your views here.
def index(response):
    reviews = Review.objects.all()
    return render(response, 'main/index.html', {'title': 'Homepage', 'reviews':reviews})

def review(response, id):
    review = Review.objects.get(id=id)
    return render(response, 'main/review.html', {'title': 'Review', 'review':review})

def find_user(response):
    if response.method == "POST":
        form = response.POST
        print(form['username'])
        user = User.objects.get(username=form['username'])
        return HttpResponse(user)

# def reviews(response):
#     reviews = Review.objects.all()
#     return render(response, 'main/allreviews.html', {'title': 'Reviews', 'reviews':reviews})

@login_required(login_url='/login/')
def new_review(response):
 
    if response.method == "POST":
        form = CreateNewReview(response.POST)

        if form.is_valid():
            rev = form.cleaned_data
            review = Review(
                user=response.user,
                product=rev['product'],
                rating=rev['rating'],
                review=rev['review'])
            review.save()
            response.user.review.add(review)
            return redirect('index')
    else:    
        form = CreateNewReview
    
    return render(response, 'main/newreview.html', {'title':'New Review', 'form':form})

@login_required(login_url='/login/')
def profile(response):
    my_profile = response.user.profile
    reviews = response.user.review.all()
    return render(response, 'main/myprofile.html', {'title':'My Profile', 'profile':my_profile, 'reviews': reviews })