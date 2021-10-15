from django.shortcuts import render
from django.http import HttpResponse
from reviewer.forms import CreateNewReview
from reviewer.models import Review

# Create your views here.
def index(response):
    print(response)
    return render(response, "main/index.html", {"title": "Homepage"})

def reviews(response):
    # reviews = Review.objects.get()
    # for review in reviews:
    #     print(review)
    return render(response, "main/reviews.html", {"title": "Reviews" })

def new_review(response):
    if response.method == "POST":
        form = CreateNewReview(response.POST)

        if form.is_valid():
            rev = form.cleaned_data
            print(rev['product'])
            review = Review(
                product=rev['product'],
                stars=rev['stars'],
                review=rev['review'])
            review.save()
    else:    
        form = CreateNewReview

    return render(response, "main/new_review.html", 
                    {"title": "New Review", "form": form})