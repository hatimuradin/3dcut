from catalog.models import Product
from myshop.models import Customer
from cart.models import CircularItem, RectangularItem, Basket
from catalog.forms import CircularProductAddToCartForm, RectangularProductAddToCartForm


def do_after_login_tasks(request, user):
    customer = Customer.objects.filter(user=request.user)[0]
    # Fetch Customer's current active basket or make new one
    customer_basket = customer.basket_set.filter(active=True).first()
    if customer_basket is None:
        customer_basket = Basket.objects.create(customer=customer)
    # Add item from session card to basket
    form_types = {
        'circular': CircularProductAddToCartForm, 
        'rectangular': RectangularProductAddToCartForm
    }
    if request.session.get('cart') is not None:
        for item in request.session['cart']:
            try:    
                product_slug = request.session['cart'][item]['product_slug']
                form = form_types[product_slug](request.session['cart'][item])
                item = form.save(commit=False)
                p = Product.objects.filter(slug=product_slug).first()
                item.product = p
                item.basket = customer_basket
                item.save()
            except:
                print('exception in saving cookie carts in database')