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

    class Meta:                      
        ordering = ['date_added']      
        
    def total(self):           
        return self.quantity * self.product.price      
        
    def name(self):           
        return self.product.name      

    def get_absolute_url(self):           
        return self.product.get_absolute_url()      
        
    def augment_quantity(self, quantity):           
        self.quantity = self.quantity + int(quantity)           
        self.save()

class CircularItem(Item):
    bar_length = models.IntegerField()
    radius = models.IntegerField()

class RectangularItem(Item):
    pass