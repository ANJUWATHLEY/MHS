from rest_framework import serializers
from mhs_app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_staff','is_active', 'email','is_superuser']  # Include only relevant fields

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Make the User serializer read-only

    class Meta:
        model = Customer
        fields = [ 'id','user', 'address', 'phone']
       

def create(self, validated_data):
  
        if 'user' not in validated_data:
            raise serializers.ValidationError({"user": "User ID is required."})
        customer = Customer.objects.create(**validated_data)
        return customer






class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"  # Serialize all fields of Product

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"  # Serialize all fields of CartItem

class CartSerializer(serializers.ModelSerializer):
    # You can include CartItems in the CartSerializer if you want to list all items in the cart
    cart_items = CartItemSerializer(many=True, read_only=True)  # Nested CartItem serializer

    class Meta:
        model = Cart
        fields = ['id', 'user', 'cart_items']  # Include relevant fields of Cart

class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer(read_only=True)  # Include Cart d
    class Meta:
         model = Order 
         fields = '__all__'