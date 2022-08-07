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
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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
def order_details(request,order_id):
    items=OrderItem.objects.all()
    order_items=items.filter(order_id=order_id)
    serializer=OrderItemSerializer(order_items, many=True) 
    return Response(serializer.data)

@api_view(['GET','POST'])
def confirm_order(request):
    user_id="0"
    if request.method=='POST':

        user_id=request.data.get("user_id")#user


        first_name=request.data.get("first_name")#customer
        last_name=request.data.get("last_name")#customer
        email=request.data.get("email")#customer
        telephone=request.data.get("telephone")#customer
        city=request.data.get("city")#customer
        post_office=request.data.get("post_office")#customer
        postal_code=request.data.get("postal_code")#customer
        street_address=request.data.get("street_address")#customer
        customer_id =request.data.get("customer_id")
        order_id =request.data.get("order_id")
       
        
        retail=request.data.get("retail")#order
        thana=request.data.get("thana")#order
        market=request.data.get("market")#order
        district=request.data.get("district")#order
        payment_method=request.data.get("payment_method")#order
        order_note=request.data.get("order_note")#order
        
        user=User.objects.get(id=user_id)

        thana=Thana.objects.get(Thana_name=retail["Thana_id"])
        district=District.objects.get(District_name=retail["District_id"])
        market=Market.objects.get(Market_name=retail["Market_id"])

        retail=Retail(id=retail["id"],Retail_name=retail["Retail_name"],Retail_Address=retail["Retail_Address"],DMS_Code=retail["DMS_Code"],
        RD_name =retail["RD_name"], RD_DMS=retail["RD_DMS"],  
        Created_Date=retail["Created_Date"],Created_By=retail["Created_By"],
        Modified_Date=retail["Modified_Date"],Modified_By =retail["Modified_By"],
        Thana_id=thana,District_id=district, Market_id=market)
        retail.save()

        customer=Customer(id=customer_id,user=user,first_name=first_name,last_name=last_name,email=email,
        telephone=telephone,city=city,post_office=post_office,postal_code=postal_code,
        street_address=street_address)
        customer.save()

        order=Order(id=order_id,order_customer=customer,retail=retail, thana=thana, market=market,
        district=district,payment_method=payment_method,
        order_note=order_note)
        order.save()
       

        products=request.data.get('products')

        orderItemList=[]
        product_list=[]
        
        for item in products:
    
            product_instance=Product.objects.get(id=item['id'])
            if product_instance.available_stock>0:
                product_instance.available_stock=product_instance.available_stock-item['quantity']
            else:
                item['quantity'] +=product_instance.available_stock
                product_instance.available_stock=0


            product_instance.save()
            product_list.append(product_instance)

            orderItemLengthSoFar=len(OrderItem.objects.all())+1

            order_item=OrderItem(id="ITEM"+str(orderItemLengthSoFar),
            order_id=order,
            quantity=item['quantity'],
            product_id=product_instance)
            
            order_item.save()
                
            orderItemList.append(order_item)
            
                
        serializer=OrderItemSerializer(orderItemList,many=True)    
        return Response(serializer.data) 

    return Response("USER ID"+user_id)  


@api_view(['POST'])
def update_stock(request):
    product_id=request.data.get('product_id')
    new_stock=request.data.get('new_stock')

    product=Product.objects.get(id=product_id)
    product.available_stock +=new_stock
    product.save()
    serializer=ProductSerializer(product,many=False) 
    return Response(serializer.data)    


@api_view(['GET'])
def orders(request):
    items=Order.objects.all()
    
    serializer=OrderSerializerWithoutCustomerDetails(items, many=True) 
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





