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
<<<<<<< HEAD
    regular_price=models.FloatField(max_length=100, null=True) 
    inventory_id=models.IntegerField( null=True) 
    discounted_price=models.FloatField(max_length=100, null=True) 
    description=models.CharField(max_length=100, unique=True, null=True) 
    available_stock=models.IntegerField() 
  
=======
    regular_price=models.FloatField(max_length=100, unique=True, null=True)

>>>>>>> ac713cb344f26b498918ab2ff243a8e4d153038d
    def __str__(self):
        return self.product_name