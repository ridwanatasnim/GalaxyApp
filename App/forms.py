from django.forms import ModelForm
from .models import *

class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


