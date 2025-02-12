from django.urls import path, include
from JewelryShop.cart import views

urlpatterns = [
    path('', '', name='cart_details'),
    path('add/', '', name='cart_add'),
    path('delete/', '', name='cart_delete'),
    path('update/', '', name='cart_update'),
]