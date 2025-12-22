from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')



def shop(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    cart_count = sum(v for v in cart.values() if isinstance(v, int))

    context = {
        'products': products,
        'cart_count': cart_count
    }
    return render(request, 'shop.html', context)

def add_shop(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            image=request.POST['image'],
            price=request.POST['price'],
            description=request.POST['description']
        )
        return redirect('myapp:shop')

    return render(request, 'shop_form.html')

def edit_shop(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.image = request.POST['image']
        product.price = request.POST['price']
        product.description = request.POST['description']
        product.save()
        return redirect('myapp:shop')

    return render(request, 'shop_form.html', {'product': product})

def delete_shop(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('myapp:shop')

    return render(request, 'shop_delete.html', {'product': product})

def product_single(request, pk):
    product = Product.objects.get(pk=pk)
    products = Product.objects.exclude(pk=pk)[:4]

    return render(request, 'product-single.html', {
        'product': product,
        'products': products,
    })



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
