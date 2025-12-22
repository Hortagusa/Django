from django.shortcuts import render, get_object_or_404, redirect
from myapp.models import Product
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProductForm
from django.contrib.auth.models import User

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

@login_required(login_url="login")
def add_shop(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("myapp:shop")
    else:
        form = ProductForm()

    return render(request, "shop_form.html", {"form": form})



@login_required(login_url="login")
def edit_shop(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("myapp:shop")
    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "shop_form.html",
        {"form": form, "product": product},
    )


@login_required(login_url="login")
def delete_shop(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('myapp:shop')

    return render(request, 'shop_delete.html', {'product': product})

def product_single(request, pk):
    product = get_object_or_404(Product, pk=pk)
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

def login_view(request):
    if request.user.is_authenticated:
        return redirect('myapp:shop')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('myapp:shop')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('myapp:shop')

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password != password2:
            messages.error(request, "Mật khẩu không khớp")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Tài khoản đã tồn tại")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )  
        return redirect("login")

    return render(request, "register.html")
