from django.shortcuts import render, reverse, redirect
from django.conf import settings
from shipping.forms import TransportForm
from django.contrib.auth.decorators import login_required
from cart.models import Customer, Basket

# Create your views here.

@login_required
def show_shipping(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = TransportForm(postdata)
        if form.is_valid():
            transaction = form.save(commit=False)
            customer = Customer.objects.filter(user=request.user)[0]
            # Fetch Customer's current active basket or make new one
            customer_basket = customer.basket_set.filter(active=True).first()
            if customer_basket is None:
                return redirect(reverse('cart:show_cart'))
            transaction.basket = customer_basket
            transaction.save()
            return redirect(reverse('payment:show_payment'))
        else:
            return render(request, "shipping/shipping.html", {'form': form, 'errors': form.errors})
    else:
        form = TransportForm()
        return render(request, "shipping/shipping.html", {'form': form})