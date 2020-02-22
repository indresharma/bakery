from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.views.generic import CreateView, DetailView

def home(request):
    prod_list = Product.objects.all()
    return render(request, 'products/home.html', {'prod_list': prod_list})


def details(request, id):
    item = Product.objects.get(pk=id)
    context = {'item': item}
    return render(request, 'products/details.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/details.html'


# def create(request):
#     form = ProductForm(request.POST)
#
#     if form.is_valid():
#         form.save()
#         return redirect('products:home')
#     return render(request, 'products/create.html', {'form': form})

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
    item = Product.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('products:home')
    return render(request, 'products/delete.html', {'item': item})





