from django.db import models
from cart.models import Basket
from utils import validators

# Create your models here.
class Transport(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    address = models.TextField()
    postal_code = models.IntegerField(validators=[validators.validate_postal_code])
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    