from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from product.models import Product
from product.forms import ProductAdminForm
from review.forms import CreateNewReview
from review.models import Review

# Create your views here.
def product(response, id):
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


# products
def product_search(response):
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
            template_name='product/products-results-partial.html',
            context={ "products": products }
        )

        html2 = render_to_string(
            template_name='product/prod-rslt-partial.html',
            context={ "products": products }
        )

        data_dict = {
            "html_for_input": html2,
            "html_from_view": html1
        }
        return JsonResponse(data=data_dict, safe=False)

    return render(response, 'main/products.html', context)


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