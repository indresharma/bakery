from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['prod_name', 'prod_desc', 'price', 'prod_image']

# class FavsForm(forms.ModelForm):
#     class Meta:
#         model = Favourites
#         fields = ['fav_prod']