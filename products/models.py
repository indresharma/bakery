from django.db import models
from django.urls import reverse
from django.conf import settings


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

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    fav_prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fav_prod