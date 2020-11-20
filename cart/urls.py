from django.urls import path, re_path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.show_cart, name='show_cart'),
    path('remove/<slug:item_id>', views.remove_item_from_cart, name='remove')
    ]