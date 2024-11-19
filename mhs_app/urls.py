# mhs_app/urls.py
from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from dj_rest_auth.views import LoginView,LogoutView
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
    path('cartitem/<int:id>/',cartitem_view,name="order-list"),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',register_view,name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

