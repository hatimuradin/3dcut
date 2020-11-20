from cart.models import Item 
from catalog.models import Product 
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
    cleaned_data['metal_types'] = cleaned_data['metal_types'].name    
    # fetch the product or return a missing page error      
    p = get_object_or_404(Product, slug=cleaned_data.get('product_slug'))
    if 'cart' not in request.session:
        request.session['cart'] = {}
    request.session['cart'][gen_order_id()] = cleaned_data
    print(request.session['cart'])       
 

