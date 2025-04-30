from django.urls import path, include
from JewelryShop.jewelries import views

urlpatterns = [
    path('add/', views.JewelriesAddView.as_view(), name='jewelry_add'),
    path('<int:pk>/', include([
        path('details', views.JewelriesDetailsView.as_view(), name='jewelry_details'),
        path('edit/', views.JewelriesEditView.as_view(), name='jewelry_edit'),
        path('delete/', views.JewelriesDeleteView.as_view(), name='jewelry_delete'),
    ])),
]