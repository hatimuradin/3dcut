from django.shortcuts import render, HttpResponse

# Create your views here.

def show_payment(request):
    return HttpResponse('hi payment')