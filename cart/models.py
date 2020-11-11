from django.db import models
from catalog.models import Product
from myshop.models import Customer

# Create your models here.

class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

class Item(models.Model):      
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)      
    date_added = models.DateTimeField(auto_now_add=True)      
    quantity = models.IntegerField(default=1)      
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE) 
    metal_type = models.ForeignKey('catalog.Metal', on_delete=models.CASCADE)
    shape_length = models.IntegerField()
    shape_x = 0

    class Meta:           
        db_table = 'cart_items'           
        ordering = ['date_added']      
        
    def total(self):           
        return self.quantity * self.product.price      
        
    def name(self):           
        return self.product.name      
        
    def price(self):           
        return self.product.price 

    def get_absolute_url(self):           
        return self.product.get_absolute_url()      
        
    def augment_quantity(self, quantity):           
        self.quantity = self.quantity + int(quantity)           
        self.save()
