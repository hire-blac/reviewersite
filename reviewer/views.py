from django.shortcuts import redirect, render
from reviewer.forms import CreateNewReview
from .models import Review

# Create your views here.
def index(response):
    reviews = Review.objects.all()
    return render(response, 'main/index.html', {'title': 'Homepage', 'reviews':reviews})

def review(response, id):
    review = Review.objects.get(id=id)
    return render(response, 'main/review.html', {'title': 'Review', 'review':review})

def reviews(response):
    reviews = Review.objects.all()
    return render(response, 'main/allreviews.html', {'title': 'Reviews', 'reviews':reviews})

def new_review(response):
    if response.method == "POST":
        form = CreateNewReview(response.POST)

        if form.is_valid():
            rev = form.cleaned_data
            print(rev['product'])
            review = Review(
                product=rev['product'],
                rating=rev['rating'],
                review=rev['review'])
            review.save()
            response.user.review.add(review)
            return redirect('my_reviews')
    else:    
        form = CreateNewReview
    
    return render(response, 'main/newreview.html', {'title':'New Review', 'form':form})

def my_reviews(response):
	return render(response, 'main/myreviews.html', {})
	