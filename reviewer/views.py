from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from register.forms import Login_Form
from reviewer.forms import CreateNewProduct, CreateNewReview
from . models import Category, Product, Review, Vote

# Create your views here.

# homepage
def index(response):
    reviews = Review.objects.all().order_by('-created')
    categories = Category.objects.all()
    user = response.user
    context = {
        'title': 'Homepage',
        'reviews':reviews,
        'categories': categories,
        'user': user
        }
    return render(response, 'main/index.html', context )

# products
def products(response):
    url_parameter = response.GET.get("q")

    if url_parameter:
        products = Product.objects.filter(name__icontains=url_parameter)
    else:
        products = 1

    context = {
        'products':products
    }

    if response.is_ajax():
        html1 = render_to_string(
            template_name='main/products-results-partial.html',
            context={ "products": products }
        )

        html2 = render_to_string(
            template_name='main/prod-rslt-partial.html',
            context={ "products": products }
        )

        data_dict = {
            "html_for_input": html2,
            "html_from_view": html1
        }
        return JsonResponse(data=data_dict, safe=False)

    return render(response, 'main/products.html', context)

# product details
def products_details(response, id):
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product=id).order_by('-created')
    form = CreateNewReview
    context = {
        'title': 'Product Details',
        'product': product,
        'reviews': reviews,
        'form': form
        }
    return render(response, 'main/product-details.html', context )

# new product
@login_required(login_url='/accounts/login/')
def new_product(response):
    if response.method == 'POST':
        form = CreateNewProduct(response.POST)
        if form.is_valid():
            prod = form.cleaned_data
            cat = Category.objects.get(id=prod['category'])
            product = Product(
                category=cat,
                name=prod['name'],
                description=prod['description'])
            product.save()
            return redirect('/products/' + str(product.id))
    else:    
        form = CreateNewProduct
        categories = Category.objects.all()

    context = {
        'title': 'New Product',
        'form': form,
        'categories': categories
    }

    return render(response, 'main/newproduct.html', context)

# single review
def review(response, id):
    review = Review.objects.get(id=id)
    context = {
        'title': 'Review',
        'review':review
        }
    return render(response, 'main/review.html', context )

# # upvote a review
@login_required(login_url='/accounts/login/')
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
        categories = Category.objects.all()
    context = {
        'title':'New Review',
        'form':form,
        # 'login_form': login_form,
        'categories': categories
        }
    return render(response, 'main/newreview.html', context )
