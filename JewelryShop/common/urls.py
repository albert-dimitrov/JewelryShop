from django.urls import path, include
from JewelryShop.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('review/<int:jewelry_id>/add/', views.AddReviewView.as_view(), name='review_add'),
    path('review/<int:pk>/delete/', views.DeleteReviewView.as_view(), name='review_delete'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('success/<int:pk>/', views.OrderSuccessView.as_view(), name='order_success'),
    path('about/', views.about_us_page, name='about'),
]