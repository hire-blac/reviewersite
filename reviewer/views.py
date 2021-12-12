from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from reviewer.forms import CreateNewReview
from .models import Profile, Review, Vote

# Create your views here.

# homepage
def index(response):
    reviews = Review.objects.all()
    user = response.user
    context = {
        'title': 'Homepage',
        'reviews':reviews,
        'user': user
        }
    return render(response, 'main/index.html', context )

# single review
def review(response, id):
    review = Review.objects.get(id=id)
    context = {
        'title': 'Review',
        'review':review
        }
    return render(response, 'main/review.html', context )

# # upvote a review
@login_required(login_url='/login/')
def upvote(response):
    user = response.user
    if response.method == 'POST':
        review_id = response.POST.get('review_id')
        review = Review.objects.get(id=review_id)
        print(user)
        if user not in review.upvotes.all():
            if user in review.downvotes.all():
                review.downvotes.remove(user)
            review.upvotes.add(user)
        else:
            review.upvotes.remove(user)

        vote, created = Vote.objects.get_or_create(user=user, review=review)

        if not created:
            if vote.value == 'Downvote':
                vote.value = 'Upvote'
        else:
            vote.value = 'Upvote'
        vote.save()

    print('Liked')
    return redirect('index')

# downvote a review
@login_required(login_url='/login/')
def downvote(response):
    user = response.user
    if response.method == 'POST':
        review_id = response.POST.get('review_id')
        review = Review.objects.get(id=review_id)
        if user not in review.downvotes.all():
            if user in review.upvotes.all():
                review.upvotes.remove(user)
            review.downvotes.add(user)
        else:
            review.downvotes.remove(user)
        
        vote, created = Vote.objects.get_or_create(user=user, review=review)

        if not created:
            if vote.value == 'Upvote':
                vote.value = 'Downvote'
        else:
            vote.value = 'Downvote'
        vote.save()
        
    print('Unliked')
    return redirect('index')

# find user
def find_user(response):
    if response.method == "POST":
        form = response.POST
        print(form['username'])
        user = User.objects.get(username=form['username'])
        return HttpResponse(user)

# def reviews(response):
#     reviews = Review.objects.all()
#     return render(response, 'main/allreviews.html', {'title': 'Reviews', 'reviews':reviews})

# create a new review
# @login_required(login_url='/login/')
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
    context = {
        'title':'New Review',
        'form':form
        }
    return render(response, 'main/newreview.html', context )

# view profile page
@login_required(login_url='/login/')
def profile(response):
    my_profile = response.user.profile
    reviews = response.user.review.all()
    context = {
        'title':'My Profile',
        'profile':my_profile,
        'reviews': reviews
        }
    return render(response, 'main/myprofile.html', context )