from django.db import models
from django.urls import reverse
from django.conf import settings

CATEGORY_CHOICES = {
    ('Cakes', 'Cakes'),
    ('Dry cakes', 'Dry Cakes'),
    ('Cookies', 'Cookies'),
}

LABEL_CHOICES = {
    ('primary', 'primary'),
    ('secondary', 'secondary'),
    ('danger', 'danger'),
}

# Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_desc = models.CharField(max_length=250)
    price = models.FloatField()
    prod_image = models.CharField(max_length=500, default="https://s3.amazonaws.com/ODNUploads/563be68403b50placeholder_food_item_2.png" )
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15) 
    label = models.CharField(choices=LABEL_CHOICES, max_length=15) 
    slug = models.SlugField()

    def __str__(self):
        return self.prod_name

    def get_absolute_url(self):
        return reverse('products:details', kwargs={'slug': self.slug})

    def add_summary(self):
        return self.prod_desc[:100]+"..."

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    fav_prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fav_prod.prod_name


#products in cart
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.prod_name}'

    def total_item_price(self):
        return self.quantity * self.item.price


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=6)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=6)
    
    def __str__(self):
        return self.user.username

#promo code
class Coupon(models.Model):
    coupon = models.CharField(max_length=10)
    discount = models.IntegerField()

    def __str__(self):
        return self.coupon

#products after checkout
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField()
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def total_price(self):
        total=0
        for order_item in self.item.all():
            total+= order_item.total_item_price()
        return total

    def discounted_price(self):
        return self.total_price()*(100-self.coupon.discount)/100
        




