from django import forms
from exset1.models import Category,Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=["category_name"]
    

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
     
        fields="__all__"

        widgets={

            "product_name":forms.TextInput(attrs={"class":"form-control"}),
             "description":forms.TextInput(attrs={"class":"form-control"}), 
             "price":forms.TextInput(attrs={"class":"form-control"})
        }



class ProductChangeForm(forms.ModelForm):

    class Meta:
        model=Product
        fields="__all__"

        widgets={

            "product_name":forms.TextInput(attrs={"class":"form-control"}),
             "description":forms.TextInput(attrs={"class":"form-control"}), 
             "price":forms.TextInput(attrs={"class":"form-control"})
        }




# class CategorySearchForm(forms.Form):
#     category_name=forms.CharField()
    
    