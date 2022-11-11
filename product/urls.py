from django.urls import path
from order.views import Create_Order,Order_Summary

urlpatterns = [
    path('createorder/', Create_Order),
    path('orders/', Order_Summary)   
]