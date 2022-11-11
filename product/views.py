from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated ,IsAdminUser ,AllowAny
from rest_framework.decorators import api_view, permission_classes 
from .models import *
# from .serializers import OrderSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from django.core import serializers

# Create your views here.

from .serializers import ProductSerializer
from .models import Product
  
# create a viewset
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    # permission_classes = (
    #     permissions.IsAuthenticated)
    
