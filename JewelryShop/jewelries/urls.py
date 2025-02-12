from django.urls import path, include
from JewelryShop.jewelries import views

urlpatterns = [
    path('add/', '', name='jewelry_add'),
    path('<int:pk>/', include([
        path('details', '', name='jewelry_details'),
        path('edit/', '', name='jewelry_edit'),
        path('delete/', '', name='jewelry_delete'),
    ])),
]