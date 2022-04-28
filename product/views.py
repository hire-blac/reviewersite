from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from product.models import Category, Product, ProductAttribValue, ProductAttribute
from product.forms import NewProductForm
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

        form = NewProductForm(response.POST)
        if form.is_valid():
            # find category
            cat = Category.objects.get(slug=form.data['category'])
            # create new product
            product = Product(
                category=cat,
                name=form.data['name'],
                image=form.data['image'],
            )
            # save product
            product.save()
            
            # loop through key,value pairs of form data queryset
            for k,i in form.data.items():
                # check if key == csrf token
                if k == "csrfmiddlewaretoken" or k == 'category' or k == 'name' or k == 'image':
                    continue
                # find product attribute
                attrib = ProductAttribute.objects.get(slug=k)
                # create new value
                val = ProductAttribValue(
                    product=product,
                    productAttribute=attrib,
                    value=i
                )
                # save value
                val.save()
            
            return HttpResponseRedirect(product.get_absolute_url())
    
    else:    
        form = NewProductForm
        
    context = {
        'title': 'New Product',
        'form': form,
        'categories': categories
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
        attribs = render_to_string(
            template_name='product/category_attrib_partial.html',
            context={ 'categoryAttributes': categoryAttributes }
        )

        data_dict = {
            "category_attributes": attribs,
        }

        return JsonResponse(data=data_dict, safe=False)

    return render(response, 'product/new-product.html', context)