from django.contrib import admin
# Register your models here.

from mhs_app.models import *
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CartItem)


