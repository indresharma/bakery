from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404

# Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc = models.CharField(max_length=250)
    price = models.IntegerField()
    prod_image = models.CharField(max_length=500, default="https://s3.amazonaws.com/ODNUploads/563be68403b50placeholder_food_item_2.png" )

    def get_absolute_url(self):
        return reverse('products:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.prod_name

# class Favourites(models.Model):
#     fav_prod = models.ForeignKey(Product, on_delete=models.CASCADE)
#
#     # def add_to_favourites(self, id):
#     #     fav = get_object_or_404(Product, pk=id)
#     #     return
#
#     def __str__(self):
#         return self.fav_prod