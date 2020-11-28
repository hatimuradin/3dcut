from django import forms
from catalog.models import Metal
from cart.models import Item, CircularItem, RectangularItem


class ProductAddToCartForm(forms.ModelForm):
    quantity = forms.IntegerField(widget=forms.TextInput(
        attrs={'size': '2', 'value': '1', 'class': 'quantity', 'maxlength': '5'}),
        error_messages={'invalid': 'Please enter a valid quantity.'},
        min_value=1)
    metal_type = forms.ModelChoiceField(queryset=Metal.objects.all(
    ), empty_label=None, to_field_name='name', widget=forms.Select(attrs={'class': 'uk-select uk-width-small'}))
    product_slug = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Item
        fields = ['quantity', 'metal_type']

"""     # override the default __init__ so we can set the request
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    # custom validation to check for cookies
    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies must be enabled.")
        return self.cleaned_data """


class CircularProductAddToCartForm(ProductAddToCartForm):
    radius = forms.IntegerField(
        required=True, label='شعاع سطح مقطع')
    bar_length = forms.IntegerField(
        required=True, label='طول میله')

    class Meta:
        model = CircularItem
        fields = ['metal_type', 'radius', 'bar_length', 'quantity']


class RectangularProductAddToCartForm(ProductAddToCartForm):
    pass
