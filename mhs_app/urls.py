# mhs_app/urls.py
from django.urls import path
from .views import Customer_view
from .views import product_view
from .views import order_view
from .views import cart_view
from . views import cartitem_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('customers/', Customer_view, name='customer-list'),           # For GET (list) and POST requests
    path('customers/<int:id>/', Customer_view, name='customer-detail'), # For GET (detail), PUT, PATCH, and DELETE requests
    path('products/', product_view, name='product_detail'),
    path('products/<int:id>/', product_view, name='product_detail'), # For GET (detail), PUT, PATCH, and DELETE requests
    path('order/',order_view,name="order-list"),
    path('order/<int:id>/',order_view,name="order-list"),
    path('cart/',cart_view,name="order-list"),
    path('cart/<int:id>/',cart_view,name="order-list"),

    path('cartitem/',cartitem_view,name="order-list"),
    path('cartitem/<int:id>/',cartitem_view,name="order-list")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

