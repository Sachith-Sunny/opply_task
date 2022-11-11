from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.utils.crypto import get_random_string

def order_number_gen():
      return str('OPP'+(get_random_string(length=5, allowed_chars='01234546789')))


class Order(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    order_number = models.CharField(max_length=9, blank=True, null=True,unique=True,default=order_number_gen)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.IntegerField(null=True,blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    
    def __str__(self) :
        return str(self.order_number)
