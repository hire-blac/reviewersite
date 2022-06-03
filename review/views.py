from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . forms import CreateNewReview, NewComment, NewReply
from . models import Comment, Reply, Review, ReviewImage, Vote
from product.models import Product


# Create your views here.

# single review
def review(response, slug1, slug):
    review = Review.objects.get(slug=slug)
    comments = review.comment.all()
    form = NewComment
    reply_form = NewReply

    context = {
        'title': 'Review',
        'review':review,
        'comments': comments,
        'form': form,
        'reply_form': reply_form
        }

    return render(response, 'review/review.html', context )

def edit_review(response, slug1, slug):
    review = Review.objects.get(slug=slug)

    # check user
    if review.user == response.user:
        context = {
            'title': 'Edit review',
            'review':review,
        }
        
        if response.method == 'POST':
            form_data = response.POST
            review.rating = form_data['rating']
            review.review = form_data['review']
            review.save()

            return HttpResponseRedirect(review.get_absolute_url())
    else:
        return HttpResponseRedirect(review.get_absolute_url())
    
    return render(response, 'review/edit-review.html', context )

# # upvote a review
@login_required(login_url='/accounts/login/')
def upvote(response):
    user = response.user
    if response.method == 'POST':
        slug = response.POST.get('slug')
        review = Review.objects.get(slug=slug)
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

    return HttpResponseRedirect(review.get_absolute_url())

# downvote a review
@login_required(login_url='/accounts/login/')
def downvote(response):
    user = response.user
    if response.method == 'POST':
        slug = response.POST.get('slug')
        review = Review.objects.get(slug=slug)
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
        
    return HttpResponseRedirect(review.get_absolute_url())

# create a new review
@login_required(login_url='/accounts/login/')
def new_review(response):
    if response.method == "POST":
        form = CreateNewReview(response.POST, response.FILES)
        print(response.FILES.getlist('image_uploads'))

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

            # loop through image files and save review images
            for f in form.files.getlist('image_uploads'):
                rev_image = ReviewImage(
                    review=review,
                    user=response.user,
                    review_image=f
                )
                rev_image.save()
                review.review_image.add(rev_image)

            response.user.review.add(review)

            return HttpResponseRedirect(product.get_absolute_url())
    else:    
        form = CreateNewReview

    context = {
        'title':'New Review',
        'form':form
        }
    return render(response, 'review/newreview.html', context )

# create a new comment
@login_required(login_url='/accounts/login/')
def new_comment(response):
    if response.method == "POST":
        form = NewComment(response.POST)

        if form.is_valid():
            comm = form.cleaned_data

            # get review object
            review = Review.objects.get(slug=response.POST.get('review'))

            comment = Comment(
                user=response.user,
                review=review,
                comment=comm['comment']
            )
            comment.save()

            # add comment to review
            review.comment.add(comment)
            
            return HttpResponseRedirect(review.get_absolute_url())
            

# create a new reply
@login_required(login_url='/accounts/login/')
def new_reply(response):
    if response.method == "POST":
        form = NewReply(response.POST)

        if form.is_valid():
            comm = form.cleaned_data

            # get review object
            comment = Comment.objects.get(id=response.POST.get('comment'))

            reply = Reply(
                user=response.user,
                comment=comment,
                reply=comm['reply']
            )
            reply.save()

            # # add user to review commenters
            # review.comments.add(response.user)

            # add comment to review
            comment.reply.add(reply)
            
            return HttpResponseRedirect(comment.review.get_absolute_url())