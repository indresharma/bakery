from django.urls import path
from . import views

app_name = 'products'

urlpatterns= [
    path('', views.home, name='home'),
    path('create/', views.CreateProductView.as_view(), name='create'),
    path('update/<slug>/', views.update_prod, name='update_prod'),
    path('delete/<slug>/', views.delete_prod, name='delete'),
    path('favourites/<slug>/', views.favourites, name='favourites'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('destruct/', views.delete_all, name='destruct'),
    path('add_to_cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', views.remove_from_cart, name='remove_from_cart'),
    path('order_summary/', views.order_summary, name='order_summary'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_coupon/', views.add_coupon, name='add_coupon'),
    path('remove_coupon/', views.remove_coupon, name='remove_coupon'),
    path('<slug>/', views.ProductDetailView.as_view(), name='details'),
    
    
]