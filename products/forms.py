from django import forms
from .models import Product

COUNTRY_CHOICES = (
    ('I', 'India'),
)

PAYMENT_CHOICES = (
    ('P', 'Paytm'),
    ('U', 'UPI'),

)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prod_name', 'prod_desc', 'price', 'prod_image', 'category', 'label', 'slug']

class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    address2 = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    country = forms.ChoiceField(choices=COUNTRY_CHOICES, widget=forms.Select(attrs={'class':'custom-select d-block w-100'}))
    state = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    zipcode = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class':'form-control'}))
    shipping_address = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    save_for_next = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    payment = forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)
 