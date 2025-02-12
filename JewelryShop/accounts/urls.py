from django.contrib.auth.views import LogoutView
from django.urls import path, include
from JewelryShop.accounts import views

urlpatterns = [
    path('login/', '', name='login'),
    path('register/', '', name='register'),
    path('logout/', '', name='logout'),
    path('profile/<int:pk>/', include([
        path('details/', '', name='profile_details'),
        path('edit/', '', name='profile_edit'),
        path('delete/', '', name='profile_delete'),
    ])),
]