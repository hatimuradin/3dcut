from django.shortcuts import render, HttpResponse

# Create your views here.

def show_shipping(request):
    return HttpResponse('hi shipping')