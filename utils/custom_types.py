from cart.models import CircularItem, RectangularItem
from catalog.forms import CircularProductAddToCartForm, RectangularProductAddToCartForm

item_form_types = {
    'circular': CircularProductAddToCartForm,
    'rectangular': RectangularProductAddToCartForm
}
item_model_types = {
    'circular': CircularItem,
    'rectangular': RectangularItem
}
