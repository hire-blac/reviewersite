from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from product.models import Product
from product.forms import ProductAdminForm
from review.forms import CreateNewReview
from review.models import Review

# Create your views here.
def product(response, id):
    # prod = Product.objects.get(id=id)
    # context = {
    #     'title': 'Product',
    #     'product': prod
    # }
    product = Product.objects.get(id=id)
    reviews = Review.objects.filter(product=id).order_by('-created')
    form = CreateNewReview
    context = {
        'title': 'Product Details',
        'product': product,
        'reviews': reviews,
        'form': form
        }

    return render(response, 'product/product.html', context)


def new_product(response):
    if response.method == 'POST':
        form = ProductAdminForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('new_product')
    else:    
        form = ProductAdminForm

    context = {
        'title': 'New Product',
        'form': form
    }

    return render(response, 'product/new-product.html', context)