from django.urls import path, re_path
from shipping import views

app_name = 'shipping'

urlpatterns = [
    path('', views.show_shipping, name='show_shipping')
    ]