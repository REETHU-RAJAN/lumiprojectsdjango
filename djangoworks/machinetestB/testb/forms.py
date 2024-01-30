from django import forms
from testb.models import Category,Products



class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"
class ProductAddForm(forms.ModelForm):
    class Meta:
        model=Products
        fields="__all__" 