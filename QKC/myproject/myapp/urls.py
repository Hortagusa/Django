from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('add/', views.add_shop, name='add_shop'),
    path('edit/<int:pk>/', views.edit_shop, name='edit_shop'),
    path('delete/<int:pk>/', views.delete_shop, name='delete_shop'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('invoice/<int:order_id>/', views.export_invoice_pdf, name='invoice_pdf'),
    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]