from catalog.models import Product
from myshop.models import Customer
from cart.models import CircularItem, RectangularItem
from catalog.forms import CircularProductAddToCartForm, RectangularProductAddToCartForm


def do_after_login_tasks(request, user):
    customer = Customer.objects.filter(user=request.user)[0]
    # Fetch Customer's current active basket or make new one
    customer_basket = customer.basket_set.filter(active=True).first()
    if customer_basket is not None:
        customer_basket = Basket.objects.create(customer=customer)
    # Add item from session card to basket
    form_types = {
        'circular': CircularProductAddToCartForm, 
        'rectangular': RectangularProductAddToCartForm
    }
    if request.session.get('cart') is not None:
        for item in request.session['cart']:
            product_slug = request.session['cart'][item]['product_slug']
            form = form_types[product_slug](request.session['cart'][item])
            item = form.save(commit=False)
            p = Product.objects.filter(product_slug=product_slug)
            item.product = p
            item.basket = customer_basket
            item.save()
