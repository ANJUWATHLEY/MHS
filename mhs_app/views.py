from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mhs_app.models import Customer
from mhs_app.models import Product
from mhs_app.models import Order
from mhs_app.models import Cart
from mhs_app.models import  CartItem

from mhs_app.serializers import *

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate,logout
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

@api_view(['POST'])
def register_view(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    phone = request.data.get('phone')
    address = request.data.get('address')
    first_name = request.data.get('first_name', '')
    last_name = request.data.get('last_name', '')


    if not all([username, email, password]):
        return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)


    
    # Create the user
    if Customer.objects.filter(user__username=username).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
    if Customer.objects.filter(user__email=email).exists():
        return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )

    Customer.objects.create(
        user=user,
        phone=phone,
        address=address
    )

    return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)

            
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def Customer_view(request, id=None):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customer_serializer = CustomerSerializer(customers, many=True)
        # variable_name = SerializerName(object_or_queryset, many=True/False)

        return Response(customer_serializer.data)
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response({"message": "Deleted successfully"})
    
    elif request.method == 'PUT':
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def product_view(request, id=None):
    if request.method == 'GET':
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True, context={"request":request})
        return Response(product_serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
   
    elif request.method == 'DELETE':
        product = Product.objects.get(product_id=id)
        product.delete()
        return Response({"message": "Deleted successfully"})



    
    elif request.method == 'PUT':
        try:
            product = Product.objects.get(product_id=id)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
    
    elif request.method == 'PATCH':
        try:
            product = Product.objects.get(product_id=id)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def order_view(request, id=None):
    if request.method == 'GET':
        if id:
            order = Order.objects.get(id=id)  # Fetch single order
            order_serializer = OrderSerializer(order)
            return Response(order_serializer.data)
        else:
            order = Order.objects.all()  # Fetch all orders
            order_serializer = OrderSerializer(order, many=True)
            return Response(order_serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)  # Create new order
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        order = Order.objects.get(id=id)  # Update entire order
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        order = Order.objects.get(id=id)  # Partial update
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        order = Order.objects.get(id=id)  # Delete order
        order.delete()
        return Response({"message": "Order deleted successfully"}, status=204)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def cart_view(request, id=None):
    if request.method == 'GET':
        if id:
            cart = Cart.objects.get(id=id)
            cart_serializer = CartSerializer(cart)
            return Response(cart_serializer.data)
        else:
            carts = Cart.objects.all()
            cart_serializer = CartSerializer(carts, many=True)
            return Response(cart_serializer.data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        cart = Cart.objects.get(id=id)
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cart = Cart.objects.get(id=id)
        cart.delete()
        return Response({"message": "Cart item deleted successfully"}, status=204)


    




@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def cartitem_view(request, id=None):
    if request.method == 'GET':
     cartitem=CartItem.objects.all()
     cartitem_serializer = CartItemSerializer(cartitem,many=True)
     return Response(cartitem_serializer.data)

    elif request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        try:
            cartitem = CartItem.objects.get(id=id)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"})

        serializer = CartItemSerializer(cartitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        try:
            cartitem = CartItem.objects.get(id=id)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"})

        serializer = CartItemSerializer(cartitem, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        try:
            cartitem = CartItem.objects.get(id=id)
        except CartItem.DoesNotExist:
            return Response({"error": "Cart item not found"})

        cartitem.delete()
        return Response({"message": "Cart item deleted successfully"})
