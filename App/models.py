from django.db import models
import datetime

# Create your models here.

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
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category=models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True) 
    product_name=models.CharField(max_length=100, unique=True, null=True) 
    regular_price=models.FloatField(max_length=100, null=True) 
    inventory_id=models.IntegerField( null=True) 
    discounted_price=models.FloatField(max_length=100, null=True) 
    description=models.CharField(max_length=100, null=True) 
    available_stock=models.IntegerField() 
    
    def __str__(self):
        return self.product_name

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