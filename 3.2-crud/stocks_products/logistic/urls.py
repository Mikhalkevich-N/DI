from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-detail-update-delete'),
    path('stocks/', views.StockListCreateView.as_view(), name='stock-list-create'),
    path('stocks/<int:pk>/', views.StockRetrieveUpdateDestroyView.as_view(), name='stock-detail-update-delete'),
]