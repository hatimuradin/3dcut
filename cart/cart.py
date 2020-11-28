from cart.models import Item 
from catalog.models import Product, Metal 
from django.shortcuts import get_object_or_404 
from django.http import HttpResponseRedirect
import decimal   # not needed yet but we will later 
import random 
import json

def gen_order_id():
    all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    order_id = random.choices(all_chars, k=10)
    return ''.join(order_id)
   
# add an item to the cart 
def add_to_cart(request, cleaned_data):
    print('inside add to cart method')
    # changing cleaned_data metal types to string for serilization
    cleaned_data['metal_type'] = cleaned_data['metal_type'].name    
    # fetch the product or return a missing page error      
    p = get_object_or_404(Product, slug=cleaned_data.get('product_slug'))
    if 'cart' not in request.session:
        request.session['cart'] = {'total_price': 0}
    cookie_item_id = gen_order_id()
    request.session['cart'][cookie_item_id] = cleaned_data
    request.session['cart'][cookie_item_id]['price'] = compute_item_price(cleaned_data)
    print(request.session['cart'])       

def compute_item_price(postdata):
    # compute item price for each type of product here
    unit_price = Metal.objects.filter(name=postdata['metal_type']).values('unit_price').first()
    return 1000

 

