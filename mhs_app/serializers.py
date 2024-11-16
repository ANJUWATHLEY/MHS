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
        # fields = [ 'name', 'email', 'phone']
        fields='__all__'

def create(self, validated_data):
        # Ensure that 'user' is included in validated_data
        if 'user' not in validated_data:
            raise serializers.ValidationError({"user": "User ID is required."})

        # Create the Customer instance with validated data
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

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"  # Serialize all fields of Order
