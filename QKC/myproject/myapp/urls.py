from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('add/', views.add_shop, name='add_shop'),
    path('edit/<int:pk>/', views.edit_shop, name='edit_shop'),
    path('delete/<int:pk>/', views.delete_shop, name='delete_shop'),
    # path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]