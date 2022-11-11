from django.db import models
from django.contrib.auth.models import User
import random, string

# Create your models here.

class Product(models.Model):
    _id = models.AutoField(primary_key=True,editable=False)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE, related_name='created_by_user', default = '1')
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    quantity_in_stock = models.IntegerField(null=True,blank=True,default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return str(self.name)


