from django.urls import path, re_path
from payment import views

app_name = 'payment'

urlpatterns = [
    path('', views.show_payment, name='show_payment')
    ]