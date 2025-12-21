from django.shortcuts import render
from .models import Product
from .forms import ProductForm
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def shop(request):
    return render(request, 'shop.html')


def product_single(request):
    return render(request, 'product-single.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def blog(request):
    return render(request, 'blog.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')
def product_add(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})
def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product_list')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
