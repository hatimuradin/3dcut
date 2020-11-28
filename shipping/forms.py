from django import forms
from shipping.models import Transport

class TransportForm(forms.ModelForm):
    #address = forms.CharField(label=_('address'))
    class Meta:
        widgets = {
          'address': forms.Textarea(attrs={'rows':2, 'cols':20, 'style':'resize:none;'}),
          'lat': forms.HiddenInput(),
          'lon': forms.HiddenInput(),
        }
        model = Transport
        fields = ['address', 'postal_code', 'lat', 'lon']