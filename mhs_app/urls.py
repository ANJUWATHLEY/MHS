# mhs_app/urls.py
from django.urls import path
from .views import Customer_view
from .views import product_view

urlpatterns = [
    path('customers/', Customer_view, name='customer-list'),           # For GET (list) and POST requests
    path('customers/<int:id>/', Customer_view, name='customer-detail'), # For GET (detail), PUT, PATCH, and DELETE requests
    path('products/', product_view, name='product_detail'),
    path('products/<int:id>/', product_view, name='product_detail'), # For GET (detail), PUT, PATCH, and DELETE requests

]

