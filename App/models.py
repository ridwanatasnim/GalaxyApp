from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.


class Thana(models.Model):
    Thana_name=models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.Thana_name 


class District(models.Model):
    District_name=models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return self.District_name         


class Market(models.Model):
    Market_name=models.CharField(max_length=100, unique=True, null=True)
    Market_Address=models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.Market_name               


class Retail(models.Model):
    
    Retail_name = models.CharField(max_length=100, unique=True, null=True)
    Retail_Address = models.CharField(max_length=200, null=True)

    DMS_Code = models.CharField(max_length=100, null=True)
    RD_name = models.CharField(max_length=100, null=True) 
    RD_DMS = models.CharField(max_length=100, null=True) 

    Created_Date = models.DateField() 
    Created_By = models.CharField(max_length=100, null=True)

    Modified_Date = models.DateField(blank=True) 
    Modified_By = models.CharField(max_length=100, blank=True) 

    Thana_id = models.ForeignKey(Thana,on_delete=models.CASCADE)
    District_id = models.ForeignKey(District,on_delete=models.CASCADE)
    Market_id = models.ForeignKey(Market,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Retail_name   

class Category(models.Model):    

    category_name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    sub_category_name=models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.sub_category_name 


class Product(models.Model):

    id=models.CharField(max_length=16, unique=True, primary_key=True) 
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True,blank=True) 
    product_name=models.CharField(max_length=100, unique=True, null=True) 
    regular_price=models.FloatField(max_length=100, null=True) 
    inventory_id=models.IntegerField( null=True) 
    discount_price=models.FloatField(max_length=100, null=True, blank=True) 
    sku=models.CharField(max_length=100, null=True) 
    description=models.CharField(max_length=100, null=True) 
    available_stock=models.IntegerField() 
    image_location=models.CharField(max_length=100, null=True) 
    
    def __str__(self):
        return self.product_name

class Customer(models.Model):

    id =models.CharField(max_length=16, unique=True,primary_key=True) 
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50, unique=True)
    telephone=models.CharField(max_length=13, unique=True)
    
    
    city=models.CharField(max_length=50)
    post_office=models.CharField(max_length=50)
    postal_code=models.CharField(max_length=10)
    street_address=models.CharField(max_length=200)
    
    
       
    def __str__(self):
        return self.email


class Order(models.Model):

    id =models.CharField(max_length=16, unique=True,primary_key=True) 

    order_customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    retail=models.ForeignKey(Retail,on_delete=models.CASCADE)
    thana=models.ForeignKey(Thana,on_delete=models.CASCADE)
    market=models.ForeignKey(Market,on_delete=models.CASCADE)
    district=models.ForeignKey(District,on_delete=models.CASCADE)

    payment_method=models.CharField(max_length=50) 
    order_note=models.CharField(max_length=50) 

    def __str__(self):
        return (self.id)
        
  

class OrderItem(models.Model):
    id =models.CharField(max_length=8, unique=True,primary_key=True)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True) 
    def __str__(self):
        return (self.id)        


