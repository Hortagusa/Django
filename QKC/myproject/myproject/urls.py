from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),

    path('product/', views.product_single, name='product_single'),

    # CRUD sản phẩm
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:id>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:id>/', views.product_delete, name='product_delete'),

    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist, name='wishlist'),

    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>/', views.blog_single, name='blog_single'),

    path('contact/', views.contact, name='contact'),
]
    