from product.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Order
from django.core import serializers
from .serializers import OrderSerializer
from rest_framework import viewsets
from django.http import HttpResponse

# create a viewset
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all() 
    serializer_class = OrderSerializer



@api_view(('GET','POST'))
def Create_Order(self):
    """Function to reduce the stock upon ordering. Checks for enough stock and product is valid too"""
    data = self.data
    try:
        product = Product.objects.get(_id = data['product'])
    except Product.DoesNotExist:
        return Response("Product does not exist")
    quantity_added = int(data['quantity'])
    if quantity_added > product.quantity_in_stock:
        return Response("Not Enough stock")
    else : 
        product.quantity_in_stock -= quantity_added
        product.save()
        user = self.user
        order_total = quantity_added * product.price
        Order.objects.create(user = user,product = product,quantity = quantity_added,total_price=order_total)
        # response = serializers.serialize('json', [ product])
        # return Response(response)
        response = serializers.serialize('json', [ product] )
        return HttpResponse(response, content_type='application/json')
   

@api_view(('GET',))
def Order_Summary(self):
    '''Function to get the order history of a user'''
    my_orders = Order.objects.filter(user__id=self.user.id).all()
    response = serializers.serialize('json',  my_orders)
    return HttpResponse(response, content_type='application/json')
   