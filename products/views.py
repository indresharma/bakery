from django.shortcuts import render, redirect
from .models import Product, Wishlist
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    prod_list = Product.objects.all()
    return render(request, 'products/home.html', {'prod_list': prod_list})


def details(request, id):
    item = Product.objects.get(id=id)
    context = {'item': item}
    return render(request, 'products/details.html', context)

@login_required
def favourites(request, id):
        item = get_object_or_404(Product, id=id)
        fav_prod, added_date = Wishlist.objects.get_or_create(fav_prod = item, user = request.user)
        messages.info(request,'The item was added to your wishlist')
        return redirect('products:details', id)

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


def update_prod(request, id):
    item = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('products:home')
    return render(request, 'products/update.html', {'form': form, 'item': item})


def delete_prod(request,id):
    item = Product.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('products:home')
    return render(request, 'products/delete.html', {'item': item})





