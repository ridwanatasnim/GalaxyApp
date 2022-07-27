from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from django.http import HttpResponse
from .models import *
from .forms import *
from .serializers import *
from .filters import *

from datetime import date
import math

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
 
# @api_view(['POST'])
# def product_queries(request):
#     products=Product.objects.all()
#     if request.method=='POST':
#         myFilter= ProductFilter(request.data, queryset=products)
       
#         products=myFilter.qs 
        
#         serializer=ProductSerializer(products, many=True)      
         
#         return Response(serializer.data)


@api_view(['POST'])
def product_queries(request):
    products=Product.objects.all()
    if request.method=='POST':
        category=request.data.get('Category')
        sub_category=request.data.get('SubCategory')
        product_name=request.data.get('Product')
       
        products = products.filter(product_name=product_name,category=category,sub_category=sub_category)


    serializer=ProductSerializer(products, many=True) 
    return Response(serializer.data)


      

