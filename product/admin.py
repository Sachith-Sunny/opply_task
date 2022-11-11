from django.contrib import admin
from .models import Product
from order.models import Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
