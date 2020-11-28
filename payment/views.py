from django.shortcuts import render

# Create your views here.

def show_payment(request):
    return render(request, "payment/payment.html")