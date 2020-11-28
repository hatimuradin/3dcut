from django.shortcuts import render, HttpResponse, redirect, reverse
from myshop.models import Customer
from cart.models import Basket, Item
from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.template import RequestContext 
from cart import cart
from django.db.models import Sum
 
def show_cart(request, template_name="cart/cart.html"):
    item_types = ['circularitem', 'rectangularitem']
    cart = {}
    #if user is authenticated show db baskets else from cookie
    if request.user.is_authenticated:
        customer = Customer.objects.filter(user=request.user)[0]
        customer_basket = customer.basket_set.filter(active=True).first()
        if customer_basket is not None:
            # Since some items have child tables in database we fetch childs data first
            joined_q = customer_basket.item_set.select_related(*item_types)
            total_price = 0
            for item in joined_q:
                for t in item_types:
                    try:
                        item_specifies = eval('item.'+t).__dict__
                        id = item_specifies['id']
                        entries_to_remove = ('_state', 'id', 'item_ptr_id', 'metal_type_id', 'date_added', 'basket_id')
                        for k in entries_to_remove:
                            item_specifies.pop(k, None)
                        cart[id] = item_specifies
                        total_price += item.price
                    except:
                        print('exception during item add to cart to show to authenticated user')
    else:
        session_cart = request.session.get('cart')
        total_price = 0
        if session_cart != None:
            for item in session_cart:
                cart[item] = session_cart[item]
                total_price += item.price
    # get cookie's basket
    return render(request, template_name, {'cart': cart, 'total_price': total_price})
    
def remove_item_from_cart(request, item_id, template_name='cart/cart.html'):
    
    if request.user.is_authenticated:
        try:
            Item.objects.filter(id=item_id).delete()
            return redirect(reverse('cart:show_cart'))
        except:
            print('exception during delete in basket when user authenticated')
        # delete item from permanent database
    else:
        try:
            del request.session['cart'][item_id]
        except:
            print('exception during delete cookie cart item user not authenticated')
        return render(request, template_name, {'cart': request.session.get('cart', {})})

    """ i think this part of code should be placed in shipping
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
    """