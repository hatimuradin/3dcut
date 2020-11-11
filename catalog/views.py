from django.shortcuts import get_object_or_404, render, redirect
from catalog.models import Category, Product, Metal
from django.urls import reverse
from cart import cart
from cart.models import Item
from catalog.forms import ProductAddToCartForm

# Create your views here.


def home_view(request, template_name="catalog/index.html"):

    context = {'page_title': 'مواد و قطعات'}
    print(context)
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
    metal_types = Metal.objects.all().values('name')
    context = {
        'metal_types': metal_types,
        'slug': p.slug,
        'meta_keywords': p.meta_keywords,
        'meta_description': p.meta_description
        }
    # need to evaluate the HTTP method
    if request.method == 'POST':
        print('post_case')
        # add to cart...create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        # check if posted data is valid
        if form.is_valid():
            # add to cart and redirect to cart page
            customer = Customer.objects.filter(user=request.user)[0]

            # Fetch Customer's current active basket or make new one
            customer_basket_count = customer.basket_set.filter(active=True).count()
            if customer_basket_count == 0:
                customer_basket = Basket.objects.create(customer=customer)
            else:
                customer_basket = customer.basket_set.filter(active=True)[0]
            # Add product to basket
            Item.objects.create()
            url = reverse('show_cart')
            return redirect(url)
    else:   
        print('get case')        
        # it’s a GET, create the unbound form. Note request as a kwarg           
        form = ProductAddToCartForm(request=request, label_suffix=':')      
        # assign the hidden input the product slug      
        form.fields['product_slug'].widget.attrs['value'] = product_slug     
        # set the test cookie on our first GET request      
        request.session.set_test_cookie() 
        context['form'] = form
        return render(request, template_name, context=context)
