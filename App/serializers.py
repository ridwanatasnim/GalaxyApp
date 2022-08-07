from rest_framework import serializers
from .models import *




class CategorySerializer(serializers.ModelSerializer):

    #id= serializers.IntegerField(required=False)
    
    class Meta:
        model = Category
        fields=["category_name"]


class SubCategorySerializer(serializers.ModelSerializer):

    #category=CategorySerializer(many=False)
    #id= serializers.IntegerField(required=False)
    
    class Meta:
        model = SubCategory
        fields=["sub_category_name",]        

class ProductSerializer(serializers.ModelSerializer):


    #category = CategorySerializer(many=False)
    #sub_category = SubCategorySerializer(many=False)
    id = serializers.CharField(required=False)
    
    class Meta:
        model = Product
        fields="__all__"


class CustomerSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Customer
        fields="__all__"


class OrderSerializer(serializers.ModelSerializer):
    
    id = serializers.CharField(required=False)
    order_customer = CustomerSerializer(many=False)
    class Meta:
        model = Order
        fields ="__all__"


class OrderSerializerWithoutCustomerDetails(serializers.ModelSerializer):
    
    id = serializers.CharField(required=False)
   
    class Meta:
        model = Order
        fields ="__all__"        


class OrderItemSerializer(serializers.ModelSerializer):
    order_id = OrderSerializer(many=False)
    product_id = ProductSerializer(many=False)
    id = serializers.CharField(required=False)
    class Meta:
        model = OrderItem
        fields = "__all__"




class ThanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thana
        fields="__all__"        


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields="__all__"       


class MarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Market
        fields="__all__"                    