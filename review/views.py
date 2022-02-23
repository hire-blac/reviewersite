from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . forms import CreateNewReview
from . models import Review, Vote
from product.models import Product


# Create your views here.

# single review
def review(response, id):
    review = Review.objects.get(id=id)
    context = {
        'title': 'Review',
        'review':review
        }
    return render(response, 'review/review.html', context )

# # upvote a review
@login_required(login_url='/accounts/login/')
def upvote(response):
    user = response.user
    if response.method == 'POST':
        review_id = response.POST.get('review_id')
        review = Review.objects.get(id=review_id)
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
@login_required(login_url='/accounts/login/')
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

# create a new review
@login_required(login_url='/accounts/login/')
def new_review(response):
    if response.method == "POST":
        form = CreateNewReview(response.POST)

        if form.is_valid():
            rev = form.cleaned_data

            # get product object
            product = Product.objects.get(name=response.POST.get('product'))

            review = Review(
                user=response.user,
                product=product,
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
    return render(response, 'review/newreview.html', context )
