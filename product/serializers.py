from rest_framework import serializers
from .models import Product
from rest_framework.serializers import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = "__all__"


