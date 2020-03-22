from django.urls import path
from . import views

app_name = 'products'

urlpatterns= [
    path('', views.home, name='home'),
    path('<slug>/', views.details, name='details'),
    path('create/', views.CreateProductView.as_view(), name="create"),
    path('update/<slug>/', views.update_prod, name='update_prod'),
    path('delete/<slug>/', views.delete_prod, name='delete'),
    path('favourites/<slug>/', views.favourites, name='favourites'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('destruct/', views.delete_all, name='destruct'),
    path('add_to_cart/<slug>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', views.remove_from_cart, name='remove_from_cart'),
    
]