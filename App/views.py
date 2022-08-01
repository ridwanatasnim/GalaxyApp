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
       
        products = products.filter(product_name=product_name)


    serializer=ProductSerializer(products, many=True) 
    return Response(serializer.data)


@api_view(['POST'])
def product_category(request):
    products=Product.objects.all()
    category=request.data.get('Category')
       
    return Response({'category':category})

   
@api_view(['GET'])
def product_group_by_category(request,category):
    Category=category
    products=Product.objects.distinct().filter(category__category_name=Category)

    serializer=ProductSerializer(products, many=True) 
    return Response(serializer.data)

   
@api_view(['GET'])
def product_group_by_sub_category(request,category,sub_category):
 
    products_category=Product.objects.distinct().filter(category__category_name=category)
    products_sub_category=products_category.filter(sub_category__sub_category_name=sub_category)
    serializer=ProductSerializer(products_sub_category, many=True) 
    return Response(serializer.data)


@api_view(['GET'])
def thana_list(request):
 
    thana_list=Thana.objects.all()
    serializer=ThanaSerializer(thana_list, many=True) 
    return Response(serializer.data)


@api_view(['GET'])
def district_list(request):
 
    district_list=District.objects.all()
    serializer=DistrictSerializer(district_list, many=True) 
    return Response(serializer.data)

@api_view(['GET'])
def market_list(request):
 
    market_list=Market.objects.all()
    serializer=MarketSerializer(market_list, many=True) 
    return Response(serializer.data)





