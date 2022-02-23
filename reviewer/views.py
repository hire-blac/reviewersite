from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from review.forms import CreateNewReview
from review.models import Review
from reviewer.forms import CreateNewProduct
from product.models import Category, Product

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
        'user': user,
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
