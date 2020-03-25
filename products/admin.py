from django.contrib import admin
from .models import Product, Wishlist, Order, OrderItem, Coupon
# Register your models here.
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Coupon)