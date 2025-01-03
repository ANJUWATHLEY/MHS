from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    phone = models.BigIntegerField()
    address=models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=225)
    price = models.IntegerField()
    images = models.ImageField(upload_to='products/')
    stock = models.IntegerField()

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')

    def __str__(self):
        return f"Cart of {self.user.username}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')

    def __str__(self):
        return f"Order {self.id} for {self.cart.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items' )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')
    quantity = models.IntegerField()
    cart_total = models.IntegerField(default=0)

    def save(self,*arg,**kwargs ):
         self.cart_total=self.product.price * self.quantity
         super().save()

    def __str__(self):
        return f"{self.quantity} x {self.product.product_name} in {self.cart}"
    
    
