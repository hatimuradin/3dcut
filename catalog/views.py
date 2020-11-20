from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from catalog.models import Category, Product, Metal
from django.urls import reverse
from cart import cart
from cart.models import CircularItem, RectangularItem, Basket
from myshop.models import Customer
from catalog.forms import CircularProductAddToCartForm, RectangularProductAddToCartForm
from django.core import serializers
from django.utils.translation import ugettext_lazy as _

# Create your views here.


def home_view(request, template_name="catalog/index.html"):

    products = Product.objects.all()
    context = {'page_title': 'مواد و قطعات', 'products': products}
    return render(request, template_name, context=context)


def show_category(request, category_slug, template_name="catalog/category.html"):

    c = get_object_or_404(Category, slug=category_slug)
    context = {
        'products': c.product_set.all(),
        'page_title': c.name,
        'meta_keywords': c.meta_keywords,
        'meta_description': c.meta_description}
    return render(request, template_name, context=context)


def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    form_types = {
        'circular': CircularProductAddToCartForm, 
        'rectangular': RectangularProductAddToCartForm
    }
    item_model_types = {
        'circular': CircularItem,
        'rectangular': RectangularItem
    }
    context = {
        'product_image': p.image,
        'slug': p.slug,
        'meta_keywords': p.meta_keywords,
        'meta_description': p.meta_description
        }
    # need to evaluate the HTTP method
    if request.method == 'POST':
        # add to cart...create the bound form
        postdata = request.POST.copy()
        form = form_types[product_slug](postdata)
        # check if posted data is valid
        if form.is_valid():
            # add to cart and redirect to cart page
            if request.user.is_authenticated: 
                customer = Customer.objects.filter(user=request.user)[0]
                # Fetch Customer's current active basket or make new one
                customer_basket = customer.basket_set.filter(active=True).first()
                if customer_basket is None:
                    customer_basket = Basket.objects.create(customer=customer)
                # Add product to basket
                item = form.save(commit=False)
                item.product = p
                item.basket = customer_basket
                item.save()
                response = redirect(reverse('cart:show_cart'))
            else:
                cart.add_to_cart(request, form.cleaned_data)
                response = redirect(reverse('cart:show_cart'))
            return response
        else:
            # do form invalid actions
            print(form.errors)
            print(form.non_field_errors)
            context['form'] = form_types[product_slug]()
            return render(request, template_name, context=context)
    else:   
        # it’s a GET, create the unbound form. Note request as a kwarg           
        form = form_types[product_slug]()   
        # assign the hidden input the product slug      
        form.fields['product_slug'].widget.attrs['value'] = product_slug    
        # set the test cookie on our first GET request      
        request.session.set_test_cookie() 
        context['form'] = form
        return render(request, template_name, context=context)
