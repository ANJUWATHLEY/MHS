from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mhs_app.models import Customer
from mhs_app.models import Product
from mhs_app.serializers import CustomerSerializer
from mhs_app.serializers import ProductSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def Customer_view(request, id=None):
    if request.method == 'GET':
        customers = Customer.objects.all()
        customer_serializer = CustomerSerializer(customers, many=True)
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
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        try:
            product = Product.objects.get(id=id)
            product.delete()
            return Response({"message": "Deleted successfully"})
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
    
    elif request.method == 'PUT':
        try:
            product = Product.objects.get(id=id)
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
            product = Product.objects.get(id=id)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)
