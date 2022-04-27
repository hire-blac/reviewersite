from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from product.models import Category, Product, ProductAttribute
from product.forms import ProductAdminForm, NewProductForm
from review.forms import CreateNewReview, NewComment
from review.models import Review

# Create your views here.
def product(response, slug):
    product = Product.objects.get(slug=slug)
    reviews = Review.objects.filter(product=product.id).order_by('-created')
    form = CreateNewReview
    comment_form = NewComment
    context = {
        'title': 'Product Details',
        'product': product,
        'reviews': reviews,
        'comment_form': comment_form,
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
    categories = Category.objects.all()
    
    if response.method == 'POST':
        #form = ProductAdminForm(response.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('new_product')
        pass
    else:    
        form = ProductAdminForm
        # book = BookForm
    context = {
        'title': 'New Product',
        'form': form,
        'categories': categories
        # 'book': book
    }

    return render(response, 'product/new-product.html', context)


def attributes_search(response):
    url_parameter = response.GET.get("category")
    category = Category.objects.get(slug=url_parameter)

    categoryAttributes = ProductAttribute.objects.filter(category=category)

    context = {
        'categoryAttributes':categoryAttributes
    }
    
    if response.is_ajax():
        print(categoryAttributes)
        attribs = render_to_string(
            template_name='product/category_attrib_partial.html',
            context={ 'categoryAttributes': categoryAttributes }
        )

        data_dict = {
            "category_attributes": attribs,
        }

        return JsonResponse(data=data_dict, safe=False)

    return render(response, 'product/new-product.html', context)