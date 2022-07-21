from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    #id= serializers.IntegerField(required=False)
    
    class Meta:
        model = Category
        fields="__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    category=CategorySerializer(many=False)
    #id= serializers.IntegerField(required=False)
    
    class Meta:
        model = SubCategory
        fields="__all__"        

class ProductSerializer(serializers.ModelSerializer):


    #category=CategorySerializer(many=False)
    sub_category=SubCategorySerializer(many=False)
    id= serializers.IntegerField(required=False)
    
    class Meta:
        model = Product
        fields="__all__"