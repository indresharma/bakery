from django.urls import path
from . import views


app_name = 'products'
urlpatterns= [
    path('', views.home, name='home'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='details'),
    path('create/', views.CreateProductView.as_view(), name="create"),
    path('update/<int:id>/', views.update_prod, name='update_prod'),
    path('delete/<int:id>/', views.delete_prod, name='delete'),
    # path('favourites/', views.favourites, name='favourites'),

]