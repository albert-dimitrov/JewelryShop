from django.urls import path, include
from JewelryShop.cart import views

urlpatterns = [
    path('', views.CartListView.as_view(), name='cart_detail'),
    path('add/<int:jewelry_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove/<int:pk>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
]