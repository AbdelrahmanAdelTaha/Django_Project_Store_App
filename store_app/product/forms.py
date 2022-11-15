from django import forms
from product.models import ProductTable

class ProductForm (forms.ModelForm):
    class Meta:
        model = ProductTable
        fields = '__all__'