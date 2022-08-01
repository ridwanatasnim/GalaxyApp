from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Thana)
admin.site.register(District)
admin.site.register(Market)
admin.site.register(Retail)

