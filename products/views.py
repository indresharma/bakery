from django.shortcuts import render, redirect
from .models import Product, Wishlist, OrderItem, Order
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime


def home(request):
    prod_list = Product.objects.all()
    return render(request, 'products/home.html', {'prod_list': prod_list})


def details(request, slug):
    item = Product.objects.get(slug=slug)
    context = {'item': item}
    return render(request, 'products/details.html', context)


@login_required
def favourites(request, slug):
    item = get_object_or_404(Product, slug=slug)
    fav_prod, added_date = Wishlist.objects.get_or_create(
        fav_prod=item, user=request.user)
    messages.info(request, 'The item was added to your wishlist')
    return redirect('products:details', slug)


@login_required
def wishlist(request):
    wished_item = Wishlist.objects.filter(user=request.user)
    return render(request, 'products/wishlist.html', {'wished_item': wished_item})


##############################  CRUD Views #####################################


class CreateProductView(CreateView):
    model = Product
    fields = ['prod_name', 'prod_desc', 'price', 'prod_image']
    template_name = 'products/create.html'

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


def update_prod(request, slug):
    item = Product.objects.get(slug=slug)
    form = ProductForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('products:home')
    return render(request, 'products/update.html', {'form': form, 'item': item})


def delete_prod(request, slug):
    item = Product.objects.get(slug=slug)

    if request.method == 'POST':
        item.delete()
        return redirect('products:home')
    return render(request, 'products/delete.html', {'item': item})


def delete_all(request):
    item_del = Product.objects.all().delete()
    return render(request, 'products/home.html', {'item_del': item_del})

###################################

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    order_qset = Order.objects.filter(user=request.user, ordered=False)

    if order_qset.exists():
        order = order_qset[0]
        if order.item.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item was updated successfully")
        else:
            order.item.add(order_item)
            messages.info(request, 'Item was added to your Cart')
    else:
        ordered_date = datetime.datetime.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.item.add(order_item)
        messages.info(request, "This item was added to your cart.")

    return redirect('products:details', slug=item.slug)

# @login_required
# def add_to_cart(request, slug):
#     item = get_object_or_404(Product, slug=slug)
#     order, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
#     ordered_date = datetime.datetime.now()
#     cart, created = Order.objects.get_or_create(user=request.user, ordered_date=ordered_date)
#     order.quantity +=1
#     cart.item.add(order)
#     order.save()
#     messages.info(request, "Item added to your cart")
#     return redirect('products: details', slug)

@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order = OrderItem.objects.get(item=item, user=request.user, ordered=False)
    cart = Order.objects.get(user=request.user)
    if order.quantity>1:
        order.quantity -=1
        messages.info(request, "Updated your cart")    
    else:
        cart.item.remove(order)
        messages.info(request, "Item removed from your cart")
    order.save() 
    return redirect('products:details', slug=item.slug)



    
