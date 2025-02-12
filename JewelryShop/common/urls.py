from django.urls import path, include
from JewelryShop.common import views

urlpatterns = [
    path('', '', name='home'),
    path('review/<int:jewelry_id>/add/', '', name='review_add'),
    path('review/<int:pk>/delete/', '', name='review_delete'),
    path('order/<int:pk>/', '', name='order_detail'),
    path('about/', '', name='about'),
]