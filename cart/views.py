from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myshop.models import Customer
from cart.models import Basket

# Create your views here.
from django.shortcuts import render
from django.template import RequestContext 
from cart import cart 
 
@login_required
def show_cart(request, template_name="cart/cart.html"):
    customer = Customer.objects.filter(user=request.user)[0]

    # Fetch Customer's current active basket or make new one
    customer_basket_count = customer.basket_set.filter(active=True).count()
    if customer_basket_count == 0:
        customer_basket = Basket.objects.create(customer=customer)
    else:
        customer_basket = customer.basket_set.filter(active=True)[0]
    basket_items = customer_basket.item_set.all()
    print(basket_items)
    context = {
        'basket_items' : basket_items,   
        'page_title' : 'Shopping Cart'
        }      
    return render(request, template_name, context=context)