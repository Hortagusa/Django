from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('product/', views.product_single, name='product_single'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_single, name='blog_single'),  # nếu cần
    path('contact/', views.contact, name='contact'),
]
